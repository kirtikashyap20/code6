from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile
from . import models
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


admin.site.register(Profile)


@admin.register(models.Punch)
class PunchAdmin(admin.ModelAdmin):
    list_display = ['user','status','punch']
    



@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['user','role','role_punch']



@admin.register(models.Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['user','status','task']