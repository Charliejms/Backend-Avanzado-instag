from django.contrib.gis.geos.mutable_list import ListMixin
from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet


class FollowingViewSet(ModelViewSet, ListMixin):
    pass
