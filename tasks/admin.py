from django.contrib import admin

from .models import Task

#register the model to the site
admin.site.register(Task)