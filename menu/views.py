from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Menu,Purchase
from .serializers import MenuSerializer,PurchaseSerializer
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework import status

# Create your views here.

class MenuList(ListAPIView):
    queryset = Menu.objects.filter(parent__isnull=True)
    serializer_class= MenuSerializer


class GetPurchaseView(APIView):
    def get(self, request):
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


class PurchaseListView(APIView):
    def post(self, request):
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


class DeletePurchaseView(APIView):
    def delete(self, request, pk):
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



        