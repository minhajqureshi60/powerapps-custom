from django.urls import path
from . import views
from .views import * 

app_name='menu'

urlpatterns = [
    path('api/menu/', views.MenuList.as_view(),name='menu-list'),
    path('api/get_purchase/',views.GetPurchaseView.as_view(),name="Get_Purchase_List"),
    path('api/purchase/',views.PurchaseListView.as_view(),name="Purchase_List"),
    path('api/delete_purchase/<int:pk>/', views.DeletePurchaseView.as_view(), name='Delete_Purchase_List'),

]