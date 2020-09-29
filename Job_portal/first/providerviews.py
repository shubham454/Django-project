from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from first.models import *


class ShowApplicant(LoginRequiredMixin, View):
    def get(self, request, id):
        global sekr
        if request.user.usertype == "Provider":
            job = Job.objects.get(pk=id)
            sekr = seeker.objects.filter(job=job)
        return render(request, "appone/showapplicant.html", {"seeker": sekr})
