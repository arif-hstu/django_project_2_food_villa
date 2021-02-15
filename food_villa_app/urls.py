'''my created url patterns'''
from django.urls import path

from . import views

app_name = 'food_villa_app'
urlpatterns = [
	# Home page
	path('', views.index, name='index'),
]
