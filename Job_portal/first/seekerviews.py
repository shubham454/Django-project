from django.shortcuts import redirect
from first.forms import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class JobApply(LoginRequiredMixin,View):
    def get(self,request):
        if request.user.usertype == 'Seeker':
            s = seeker.objects.get(user = request.user)
            s.job.add(Job.Objects.get(pk = id))
            s.save()
        return redirect('/profile/')