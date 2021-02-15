from django.contrib import admin

# Import my models
from .models import Topic, Item

# Register your models here.
admin.site.register(Topic)
admin.site.register(Item)
