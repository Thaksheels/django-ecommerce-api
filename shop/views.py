from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from shop.models import Cart, Category,Product, Shipment
from shop.serializers import CategorySerializer, PaymentSerializer,ProductSerializer,CartSerializer, ShipmentSerializer
from instamojo_wrapper import Instamojo


API_KEY ='test_b2ccbec82235d11b609cbb10869'
AUTH_TOKEN = 'test_44581cb098b82108afc82655aea'

api = Instamojo(api_key=API_KEY,auth_token=AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')


# Create your views here.

@api_view(["GET"])
def get_category(request):
    
    category_list = Category.objects.all()
    serialize_category = CategorySerializer(category_list, many=True)
    return Response({'category': serialize_category.data})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_product(request):
    print(request.user.is_staff)
    
    product_list = Product.objects.all()
    serialize_product = ProductSerializer(product_list, many=True)

    # Get base URL or hostname from Django settings
    base_url = request.get_host()  # Replace BASE_URL with your actual settings variable

    # Manipulate each todo item to include the full URL for the image
    for product in serialize_product.data:
        print(product)
        
        if 'image' in product and product['image']:  # Assuming 'img' is the key for your image path in the serialized data
            product['image'] = product['image']

    
    return Response({'message':'product fetched successfully','product': serialize_product.data,'status':True})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_cart(request):
    
    if request.method == "POST":
        request.data["customer"]=request.user.id
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'product added to cart'})
        else:
            print(serializer.errors)
    return Response({'message':'product fetched successfully'})


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_cart(request,pk):
    
    if request.method == "PUT":
        
        print(request)
        try:
            cart = Cart.objects.get(cart_id=pk,customer=request.user)
            print(cart)
            serializer=CartSerializer(cart,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'cart updated successfully'})
        except Cart.DoesNotExist:
            return Response({'message':'cart does not exist'})
    return Response({'message':'product fetched successfully'})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def shipment_details(request):

    if request.method == "POST":
            request.data["customer"]=request.user.id
            serializer=ShipmentSerializer(data=request.data)
            if serializer.is_valid():
                    serializer.save()
                    return Response({'message':'saved shipment details'})
            else:
                    print(serializer.errors)

        
        
    return Response({'message':'product fetched successfully'})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_shipment_details(request):
    
    if request.method == "GET":
        
        print(request)
        try:
            shipment = Shipment.objects.filter(customer=request.user)
            
            serializer=ShipmentSerializer(shipment,many=True)
            
            return Response({'message':'details fetched successfully','details':serializer.data})
            
        except Cart.DoesNotExist:
            return Response({'message':'shipment does not exist'})
    return Response({'message':'product fetched successfully'})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def pay_and_place_order(request):

    if request.method == "POST":
        #     amount = request.data.get('amount')
        #     response = api.payment_request_create(
        #     amount=amount,
        #     purpose="shopping",
        #     buyer_name="name",
        #     send_email=True,
        #     email="thaksheelspillai@gmaill.com",
        #     redirect_url='http://127.0.0.1:8003/success/'
        # )
        #     print(response)
            return HttpResponseRedirect("https://pypi.org/project/instamojo-wrapper/")

        
        
    return Response({'message':'product fetched successfully'})

        
        
    