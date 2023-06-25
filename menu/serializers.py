from rest_framework import serializers
from .models import Menu,Purchase


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        #fields=('id','name','parent')
        fields='__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields='__all__'
