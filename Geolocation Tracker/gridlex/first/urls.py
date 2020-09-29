from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page, name='home'),
    path('add_place/', views.AddPlaces.as_view(), name='add_place'),
    path('locations/', views.AllLocation.as_view(), name='locations'),
    path('<place_name>/', views.find_nearest_distance, name='distance')
]