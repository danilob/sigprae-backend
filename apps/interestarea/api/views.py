# flavors/api/views.py
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from rest_framework.views import APIView
from rest_framework.response import Response

# from rest_framework.permissions import IsAuthenticated
from ..models import InterestArea
from .serializers import InterestAreaSerializer
from apps.subject.models import Subject

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class InterestAreaListCreateAPIView(ListCreateAPIView):
    queryset = InterestArea.objects.all()
    # permission_classes = (IsAuthenticated, )
    serializer_class = InterestAreaSerializer
    lookup_field = 'uuid'  # Don't use InterestArea.id!
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class InterestAreaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = InterestArea.objects.all()
    # permission_classes = (IsAuthenticated, )
    serializer_class = InterestAreaSerializer
    lookup_field = 'uuid'  # Don't use InterestArea.id!



class InterestAreaQueriesAPIView(APIView):
    
    def get(self, request, uuid, format=None):
        subject = Subject.objects.get(uuid=uuid)
        interestareas = subject.interestareas.all()
        serializer = InterestAreaSerializer(interestareas, many=True)
        return Response(serializer.data) 