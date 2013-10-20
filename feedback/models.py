from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    information = models.TextField()


