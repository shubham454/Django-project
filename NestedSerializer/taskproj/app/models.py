from django.db import models


class Member(models.Model):
    member = models.CharField(max_length=64, primary_key=True)
    real_name = models.CharField(max_length=64)
    tz = models.CharField(max_length=256)

    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):
    member = models.ForeignKey(Member,
                               on_delete=models.CASCADE,
                               related_name='activity_periods')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()