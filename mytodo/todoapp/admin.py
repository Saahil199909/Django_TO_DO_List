from django.contrib import admin
from .models import Users, Task

# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'password', 'phone')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','task_name', 'user', 'date', 'status')