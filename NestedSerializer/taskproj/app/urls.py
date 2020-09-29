from django.urls import path
from . import views

urlpatterns = [
    path('member', views.MemberListView.as_view(),
         name='member_list'),
]