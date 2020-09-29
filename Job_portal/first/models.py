from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from job_portal import settings


# Create your models here.
class User(AbstractUser):
    user_choice = (('Provider', 'Provider'), ('Seeker', 'seeker'))
    usertype = models.CharField(max_length=10, choices=user_choice, default='Seeker')

    def __str__(self):
        return self.username


class Provider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField()
    company_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Job(models.Model):
    user_choice = (('Mech', 'mech'), ('Civil', 'civil'), ('IT', 'IT'))
    title = models.CharField(max_length=50)
    stream = models.CharField(max_length=50, choices=user_choice)
    desc = models.TextField(max_length=100)
    experience = models.FloatField()
    date = models.DateField(default=datetime.date.today)
    date_end = models.DateField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Seeker(models.Model):
    user_choice = (("Mech", "mech"), ("Civil", "civil"), ("IT", "IT"))
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    looking_job_in = models.CharField(max_length=50, choices=user_choice)
    job = models.ManyToManyField(Job)

    def __str__(self):
        return self.user.username
