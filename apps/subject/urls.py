from django.urls import path

from apps.subject.api import views

urlpatterns = [
   # /subject/api/
   path(
       route='api/',
       view=views.SubjectListCreateAPIView.as_view(),
       name='subject_rest_api_create_or_list'
   ),
   # /subject/api/:uuid/
   path(
       route='api/<uuid:uuid>/',
       view=views.SubjectRetrieveUpdateDestroyAPIView.as_view(),
       name='subject_rest_api_update_or_delete'
    ),
   # /subject/api/:uuid/interestarea/
   path(
       route='api/<uuid:uuid>/interestarea/',
       view = views.SubjectQueriesAPIView.as_view(),
       name='subject_rest_api_by_interestarea'
   ),
   # /subject/api/:slug/interestarea/
   path(
       route='api/<slug:slug>/interestarea/',
       view = views.SubjectQueriesAPIView.as_view(),
       name='subject_rest_api_by_interestarea'
   ),
   # /subject/api/interestarea/
   path(
       route='api/interestarea/',
       view = views.SubjectQueriesAPIView.as_view(),
       name='subject_rest_api_by_interestarea'
   ),
   # /subject/api/similar/
   path(
       route='api/similar/',
       view = views.SubjectQueriesFilterAPIView.as_view(),
       name='subject_search_api_by_text'
   ),
   # /subject/api/exact/
   path(
       route='api/exact/',
       view = views.SubjectQueriesExactFilterAPIView.as_view(),
       name='subject_exact_search_api_by_text'
   )
]