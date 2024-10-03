
from django.urls import path
from shop import views



urlpatterns = [
    path('categorylist/', views.get_category),
    path('productlist/', views.get_product),
    path('addcart/', views.add_cart),
    path('getcart/', views.get_cart),
    path('updatecart/<int:pk>/', views.update_cart),
    path('shipmentdetails/', views.shipment_details),
    path('fetchshipmentdetails/', views.fetch_shipment_details),
    path('paymentdetails/', views.pay_and_place_order)



]
