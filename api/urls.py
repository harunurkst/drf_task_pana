from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^divisions/', views.DivisionsList.as_view()),
    url(r'^districts/', views.DistrictsList.as_view()),
    url(r'^thana/', views.ThanaList.as_view()),

]
