from django.urls import path
from . import views 

urlpatterns=[
    path('', views.home, name='home'),
    path('api/user-data', views.user_data, name='user_data'),
]