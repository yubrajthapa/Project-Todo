from django.contrib import admin
from app_todo.models import *

# Register your models here.
class Details(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'email', 'password', 'contact')

admin.site.register(UserDetails,Details)
admin.site.register(UserTodo)