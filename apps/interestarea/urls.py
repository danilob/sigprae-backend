from django.urls import path

from apps.interestarea.api import views

urlpatterns = [
   # /flavors/api/
   path(
       route='api/',
       view=views.InterestAreaListCreateAPIView.as_view(),
       name='interest_area_rest_api'
   ),
   # /flavors/api/:uuid/
   path(
       route='api/<uuid:uuid>/',
       view=views.InterestAreaRetrieveUpdateDestroyAPIView.as_view(),
       name='interest_area_rest_api'
    ),
    # /interestarea/api/:uuid/subject/
   path(
       route='api/<uuid:uuid>/subject/',
       view = views.InterestAreaQueriesAPIView.as_view(),
       name='interestarea_rest_api_by_subject'
   )
]