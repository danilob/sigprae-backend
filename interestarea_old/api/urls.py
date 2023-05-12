from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('interestarea/api/sayhi/',hello_world),
	path('interestarea/api/list', get_intereset_areas),
]
