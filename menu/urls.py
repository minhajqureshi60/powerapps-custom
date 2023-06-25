from django.urls import path
from . import views
from .views import * 

app_name='menu'

urlpatterns = [
    path('api/menu/', views.MenuList.as_view(),name='menu-list'),
    path('api/get_purchase/',views.get_purchase,name="Get_Purchase_List"),
    path('api/purchase/',purchase_list,name="Purchase_List"),
    path('api/delete_purchase/<int:pk>/', views.delete_purchase, name='Delete_Purchase_List'),

]