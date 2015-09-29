from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ApiKey(models.Model):
    user = models.ForeignKey(User, unique=True)
    key = models.CharField(max_length=64)
    created_at = models.DateTimeField('created at')