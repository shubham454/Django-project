import csv
from geopy.geocoders import Nominatim
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gridlex.settings')
import django
django.setup()
from first.models import Agent


def create_record():
    """
    this function is use only to create record in first run
    """
    tsv_file = open('agents.tsv')
    read_tsv = csv.reader(tsv_file, delimiter='\t')
    for row in read_tsv:
        address = row[3]
        locator = Nominatim(user_agent='first')
        location = locator.geocode(address)
        Agent.objects.create(name=row[1],
                             address=row[2],
                             city=row[3],
                             zipcode=row[4],
                             state=row[5],
                             longitude=location.longitude,
                             latitude=location.latitude)
    print('completed')


create_record()
