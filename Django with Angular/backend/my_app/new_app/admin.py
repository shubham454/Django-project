from django.contrib import admin
from new_app.models import Tutorial

@admin.register(Tutorial)
class TutorialAdminModel(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'published']