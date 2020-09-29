from django.shortcuts import render, redirect
from first.forms import *
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


# Create your views here.
class HomeView(TemplateView):
    template_name = 'first/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['username'] = User.objects.get


class UserRegistration(View):
    def get(self, request):
        form = UserRForm()
        return render(request, 'first/reg.html', {'form': form, 'register': True})

    def post(self, request):
        form = UserRForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successfully please LogIn to continue')
            return render(request, 'first/home.html', {'form': form, 'messages': messages})
        return render(request, 'first/reg.html', {'form': form})


class Profile(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        if request.user.usertype == 'Provider':
            user1 = User.objects.get(username=request.user.username)
            try:
                p = Provider.objects.get(user=user1)
            except:
                p = None
            try:
                j = Job.objects.all(provider=p)
            except:
                j = None
            if p == None:
                return redirect('/addp/')
            return render(request, 'first/profile.html', {'p': p, 'j': j, 'isProvider': True})
        if request.user.usertype == 'Seeker':
            user1 = User.objects.get(username=request.user.username)
            try:
                s = Seeker.objects.get(user=user1)
            except:
                s = None
            if s == None:
                return redirect('/addp/')
            try:
                j = Job.objects.filter(stream=s.looking_job_in)
            except Exception as e:
                j = None
            try:
                appied = s.job.all()
            except Exception as e:
                appied = None
            return render(request, 'first/profile.html', {'p': s, 'job': j, 'isSeeker': True, 'applied': applied})
        return redirect('')


class ProfileAdd(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        if request.user.usertype == 'Provider':
            form = ProviderForm()
        if request.user.usertype == 'Seeker':
            form = SeekerForm()
        return render(request, 'first/provider.html', {'form': form})

    def post(self, request):
        if request.user.usertype == 'Provider':
            form = ProviderForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get("email")
                company_name = form.cleaned_data.get("company_name")
                Provider.objects.create(user=User.objects.get(username=request.user.username),
                                        email=email, company_name=company_name)
        if request.user.usertype == "Seeker":
            form = SeekerForm(request.POST)
            if form.is_valid():
                looking_job_in = form.cleaned_data.get("looking_job_in")
                fname = form.cleaned_data.get("fname")
                lname = form.cleaned_data.get("lname")
                s = seeker(user=User.objects.get(username=request.user.username),
                           looking_job_in=looking_job_in, fname=fname, lname=lname)
                s.save()
        return redirect('/profile/')


class AddJob(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.usertype == 'Provider':
            form = JobForm()
            return render(request, 'first/addjob.html', {'form': form})
        return redirect('/index/')

    def post(self, request):
        if request.user.usertype == 'Provider':
            form = JobForm(request.POST)
            if form.is_valid():
                form.save()
        return redirect('/profile/')
