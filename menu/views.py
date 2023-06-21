from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Menu
from .serializers import MenuSerializer

# Create your views here.

class MenuList(ListAPIView):
    queryset = Menu.objects.filter(parent__isnull=True)
    serializer_class= MenuSerializer
