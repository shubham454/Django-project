from django.shortcuts import render, HttpResponse, redirect
from .models import Agent, Places
from .forms import PlacesForm
from django.views import View
from django.views.generic import ListView
from geopy.geocoders import Nominatim
from geopy.distance import distance, vincenty


def first_page(request):
    return render(request, 'first/home.html')


class AddPlaces(View):
    """
    this class use to add places in place model to search for agent
    """
    def get(self, request):
        form = PlacesForm()
        return render(request, 'first/add_place.html', {'form': form})

    def post(self, request):
        """
        this function will find and save Longitude and latitude od the address
        """
        form = PlacesForm(request.POST)
        place_name = request.POST.get('place_name')
        locator = Nominatim(user_agent='myGeocoder')
        location = locator.geocode(place_name)
        form.longitude = location.longitude
        form.latitude = location.latitude
        if form.is_valid():
            Places.objects.create(place_name=place_name,
                                  longitude=location.longitude,
                                  latitude=location.latitude)
            return redirect('/add_place/')
        return render(request, 'first/add_place.html', {'form.errors': form.errors})


class AllLocation(ListView):
    model = Places
    context_object_name = 'places'


def find_nearest_distance(request, place_name=None):
    place = Places.objects.get(place_name=place_name)
    agents = Agent.objects.all()
    agent_dict = dict()
    for agent in agents:
        dist = distance((place.latitude, place.longitude), (agent.latitude, agent.longitude))
        agent_dict[agent.name] = dist
    nearest_agent = {k: v for k, v in sorted(agent_dict.items(), key=lambda item: item[1])}
    return render(request, 'first/agents.html', {'nearest_agent': nearest_agent})
