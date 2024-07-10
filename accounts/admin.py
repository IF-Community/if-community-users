from django.contrib import admin
from .models import Profile, Report

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    pass