from django.contrib import admin
from .models import Agent, Places


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'city', 'longitude', 'latitude')


@admin.register(Places)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_name', 'longitude', 'latitude')