from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class School(models.Model):
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    town = models.CharField(max_length=255)
    clases = models.JSONField()
    lessons = models.JSONField()
    class_form = models.JSONField()
    lesson_form = models.JSONField()
    password = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add = True)
    time_update = models.DateTimeField(auto_now= True)
class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    age = models.IntegerField()
    birthday = models.DateField()
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    number_phone = models.CharField(max_length=255)
    name_parrent1 = models.CharField(max_length=255)
    name_parrent2 = models.CharField(max_length=255)
    number_phone_parrent1 = models.CharField(max_length=255)
    number_phone_parrent2 = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    work_parrent1 = models.CharField(max_length=255)
    work_parrent2 = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add = True)
    time_update = models.DateTimeField(auto_now= True)
# class SchoolClass(models.Model):
#     title = models.CharField(max_length=255)
#     rank = models.IntegerField()
#     schedule = models.JSONField()
#     studensts = models.JSONField()
#     lessons = models.JSONField
#     time_create = models.DateTimeField(auto_now_add = True)
#     time_update = models.DateTimeField(auto_now= True)