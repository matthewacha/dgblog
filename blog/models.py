from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User

# Create your models here.
# class Author(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE, editable=False)

class Post(models.Model):
    title = models.fields.CharField(max_length=100, null=True, blank=True)
    body = models.fields.CharField(max_length=2000, null=True, blank=True)
    author = models.fields.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
