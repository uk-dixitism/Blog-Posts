from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank = True)
    username = models.CharField(max_length=50, null=True)