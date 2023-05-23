# flavors/api/views.py
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from django.http.response import HttpResponseServerError


from rest_framework.response import Response
from rest_framework.views import APIView

# from rest_framework.permissions import IsAuthenticated
from ..models import Subject
from .serializers import *
from apps.interestarea.models import InterestArea
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class SubjectListCreateAPIView(ListCreateAPIView):
    queryset = Subject.objects.all()
    # permission_classes = (IsAuthenticated, )
    serializer_class = SubjectSerializer
    lookup_field = 'uuid'  # Don't use Subject.id!
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']

class SubjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    # permission_classes = (IsAuthenticated, )
    serializer_class = SubjectSerializer
    lookup_field = 'uuid'  # Don't use Subject.id!

class SubjectQueriesAPIView(APIView):
    def get(self, request, uuid, format=None):
        interestarea = InterestArea.objects.get(uuid=uuid)
        subjects = interestarea.subjects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

class SubjectQueriesFilterAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # queryset = Subject.objects.all()

        check_description=self.request.query_params.get('check_description',None)
        if check_description:
            queryset = Subject.objects.filter(description__icontains=check_description)
            serializer = SubjectQueriesFilterSerializer(queryset,many=True)
            return Response(serializer.data)
        return Response([])

class SubjectQueriesExactFilterAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # queryset = Subject.objects.all()

        check_description=self.request.query_params.get('check_description',None)
        if check_description:
            queryset = Subject.objects.filter(description__iexact=check_description)
            serializer = SubjectQueriesFilterSerializer(queryset,many=True)
            return Response(serializer.data)
        return Response([])


    
    # def get(self, request, slug, format=None):
    #     interestarea = InterestArea.objects.get(slug=slug)
    #     subjects = interestarea.subjects.all()
    #     serializer = SubjectSerializer(subjects, many=True)
    #     return Response(serializer.data)
    
    # def get(self, request, format=None):
    #     try:
    #         interestarea = InterestArea.objects.get(slug=request.data['slug'])
    #         subjects = interestarea.subjects.all()
    #         serializer = SubjectSerializer(subjects, many=True)
    #     except Exception as e:
    #         return HttpResponseServerError(e)
    #     return Response(serializer.data)
