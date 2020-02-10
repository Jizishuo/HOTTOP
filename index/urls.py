# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path("type/<str:type>/<int:type_id>", views.Sprider_type.as_view(), name='sprider'),
]