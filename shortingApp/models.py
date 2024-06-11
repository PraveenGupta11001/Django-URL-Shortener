# models.py
from django.db import models
import string
import random

def generate_unique_token(length = 8):
    characters = string.ascii_letters + string.digits
    while True:
        token = ''.join(random.choices(characters, k=length))
        if not URL.objects.filter(token=token).exists():
            return token

class URL(models.Model):
    original_url = models.URLField(max_length=200)
    token = models.CharField(max_length=10, unique=True, default=generate_unique_token)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_url} -> {self.token}"
