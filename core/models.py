from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    language_code = models.CharField(max_length=10, blank=True, null=True)
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"@{self.username}" if self.username else f"{self.first_name} ({self.telegram_id})"

class myuser(models.Model):
    username=models.CharField(max_length=100)
    ids=models.IntegerField( max_length=20)
    ballance=models.FloatField()

    def __str__(self):
        return self.name