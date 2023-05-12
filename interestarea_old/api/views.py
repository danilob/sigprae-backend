from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from interestarea.models import InterestArea

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})



@api_view()
def get_intereset_areas(request):
    areas = InterestArea.objects.all()
    dict_response = {}
    for area in areas:
        dict_response['name'] = area.title
    return Response(dict_response)