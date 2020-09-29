import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskproj.settings')
import django

django.setup()
from faker import Faker
import datetime
from app.models import Member, ActivityPeriod

fake = Faker()


def populate(n):
    for i in range(n):
        member = fake.random_number(digits = 5)
        real_name = fake.name()
        tz = fake.address()
        start_time = fake.date_time()
        end_time = fake.date_time()
        Member.objects.get_or_create(member=member,
                                     real_name=real_name,
                                     tz=tz)
        ActivityPeriod.objects.create(member=Member.objects.get(member=member,
                                                                real_name=real_name,
                                                                tz=tz),
                                      start_time=start_time,
                                      end_time=end_time)


populate(20)
