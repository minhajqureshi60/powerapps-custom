from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Menu
from .serializers import MenuSerializer
from django.db import models

# Create your views here.

class MenuList(ListAPIView):
    queryset = Menu.objects.filter(parent__isnull=True)
    serializer_class= MenuSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PurchaseSerializer
from datetime import date
from .models import Purchase

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Purchase
from .serializers import PurchaseSerializer
from rest_framework.decorators import api_view
from django.db.models import Sum

@api_view(['GET'])
def get_purchase(request):
    try:
        purchases = Purchase.objects.all()
        serializer = PurchaseSerializer(purchases, many=True)
        return Response({
            'status': True,
            'message': 'Success',
            'data': serializer.data
        })
    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'message': 'Something went wrong'
        })


@api_view(['POST'])
def purchase_list(request):
    try:
        data = request.data
        serializer = PurchaseSerializer(data=data)
        if serializer.is_valid():
            purchase = serializer.save()

            # Calculate total for the current purchase
            total = purchase.number_of_bottles * purchase.rupees

            # Calculate total number_of_bottles present in the database
            total_bottles = Purchase.objects.aggregate(Sum('number_of_bottles'))['number_of_bottles__sum']

            # Calculate grand total by adding all number_of_bottles fields
            grand_total = Purchase.objects.aggregate(Sum('rupees'))['rupees__sum']

            return Response({
                'status': True,
                'message': 'Success',
                'data': {
                    'id': purchase.id,
                    'date': purchase.date,
                    'number_of_bottles': purchase.number_of_bottles,
                    'rupees': purchase.rupees,
                    'total': total,
                    'total_bottles': total_bottles,
                    'grand_total': grand_total,
                }
            })

        return Response({
            'status': False,
            'message': 'Invalid Data',
            'data': serializer.errors
        })

    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'Something went wrong'
    })


@api_view(['DELETE'])
def delete_purchase(request, pk):
    try:
        purchase = Purchase.objects.get(pk=pk)
        purchase.delete()
        return Response({
            'status': True,
            'message': 'Data deleted successfully'
        })
    except Purchase.DoesNotExist:
        return Response({
            'status': False,
            'message': 'Data not found'
        })
    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'message': 'Something went wrong'
        })



        