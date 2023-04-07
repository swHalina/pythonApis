from django.urls import path
from . import views

urlpatterns = [
    path('api/person/', views.PersonList.as_view(), name='person_list'),
    path('api/person/<int:pk>/', views.PersonDetail.as_view(), name='person_detail'),
]