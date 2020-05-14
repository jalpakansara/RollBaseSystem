from django.db import models
from django_mysql.models import ListTextField

# Create your models here.

designation = [
    ('Principal', 'Principal'),
    ('Teacher', 'Teacher'),
    ('Student', 'Student')
]

class User(models.Model):
    designation = models.CharField(choices=designation, max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    device = ListTextField(models.CharField(max_length=100),blank=True,null=True, default=list)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)

class Admin(models.Model):
    designation = models.CharField(max_length=255,default="Admin")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    device = ListTextField(models.CharField(max_length=100),blank=True, null=True, default=list)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)

class Tutorial(models.Model):
    Student = models.ManyToManyField(to=User)
    Teacher = models.EmailField(null=True)
    room = models.CharField(max_length=225, null=True, blank=True)
    subject = models.CharField(max_length=225, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)