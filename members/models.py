# import re
# from django.core import validators
from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.utils import timezone




class Member(AbstractUser):
    faculty_number = models.CharField(max_length=8, unique=True)
