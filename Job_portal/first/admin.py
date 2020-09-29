from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from first.models import *

# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Provider)
admin.site.register(Seeker)
admin.site.register(Job)
