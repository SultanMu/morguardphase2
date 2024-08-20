from django.db import models
from pgvector.django import VectorField
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Company(models.Model):
    index_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=300)
    title = models.CharField(max_length=300,default="0")
    date = models.DateField(null=True)
    next_asses_date = models.CharField(max_length=300,default="NA")
    company = models.CharField(max_length=300,default="NA")
    author = models.CharField(max_length=300,default="NA")
    description = models.CharField(max_length=1000,null=True)

# class MguardFileEmbeddings(models.Model):
#     gpt_embeddings = VectorField(
#         dimensions=1536,
#         help_text="Vector embeddings for file content",
#         null=True,
#         blank=True,
#     )