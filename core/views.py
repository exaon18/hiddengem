from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import TelegramUser

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def user_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            telegram_data = data.get('telegram_data')
            print(telegram_data)
            
            if telegram_data and 'initData' in telegram_data:
                from urllib.parse import parse_qsl, unquote
                
                init_data = unquote(telegram_data['initData'])
                params = dict(parse_qsl(init_data))
                
                user_info_str = params.get('user', '{}')
                user_info = json.loads(user_info_str)

                # Get or create the user in the database
                user, created = TelegramUser.objects.update_or_create(
                    telegram_id=user_info.get('id'),
                    defaults={
                        'first_name': user_info.get('first_name'),
                        'last_name': user_info.get('last_name'),
                        'username': user_info.get('username'),
                        'language_code': user_info.get('language_code'),
                        'is_premium': user_info.get('is_premium', False),
                    }
                )
                
                if created:
                    print(f"Created new user: {user}")
                else:
                    print(f"Updated user: {user}")


            return JsonResponse({'status': 'success', 'message': 'Data received and user saved'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
