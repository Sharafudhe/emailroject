from django.db import models

class MailForm(models.Model):
    Name = models.CharField(max_length=255)
    Age = models.IntegerField()
    Password = models.CharField(max_length=255)
    Email = models.EmailField()
    Address = models.TextField()

