from django.db import models
from pgvector.django import VectorField
from django.contrib.auth.models import AbstractBaseUser
from datetime import datetime
class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Company(models.Model):
    type = models.CharField(max_length=300)
    title = models.CharField(max_length=300,default="0")
    created_date = models.CharField(max_length=50,default="NA")
    next_asses_date = models.CharField(max_length=50,default="NA")
    company = models.CharField(max_length=300,default="NA")
    author = models.CharField(max_length=300,default="NA")
    summary = models.CharField(max_length=2000,null=True)
    file_name = models.CharField(max_length=100,null=True)
    flag = models.BooleanField("flag")
    date_processed = models.DateField(default=str(datetime.date(datetime.now())))

# class MguardFileEmbeddings(models.Model):
#     gpt_embeddings = VectorField(
#         dimensions=1536,
#         help_text="Vector embeddings for file content",
#         null=True,
#         blank=True,
#     )