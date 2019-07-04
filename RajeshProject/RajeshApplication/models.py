from django.db import models

# Create your models here.
class UserData(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    states =  models.CharField(max_length=100)
    subject = models.CharField(max_length=1000)


class FeedbackData(models.Model):
    name = models.CharField(max_length=100)
    work_rating = models.BigIntegerField()
    date = models.DateTimeField(max_length=100)
    feedback = models.CharField(max_length=1000)