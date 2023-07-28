from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *

# restframework & serializers
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.serializers import ProductListSerializer, ProductDetailSerializer, CategoryListSerializer
# Create your views here.
from .basket import Basket


class HomeView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "product/home.html"
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["brands"] = Brand.objects.all()
        return context
    


class ProductListView(ListCreateAPIView):
    serializer_class = ProductListSerializer


    def get_queryset(self):
        products = Product.objects.all()
        brand = self.request.query_params.get("brand")
        if brand:
            products = products.filter(brand=brand)
        
        return products


class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "id"


class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


@api_view(['GET'])
def basket_summary(request): 
    basket = Basket(request)
    print(basket.basket)
    return Response(basket)



@api_view(['POST'])
def basket_update(request):
    data = {"key":"value"}
    request.session["basket-data"] = data
    print("testing session" ,request.session.items())  # Check session data

    if request.data.get('action') == 'add':
        print("adding")
        print(request.data)
        basket = Basket(request) 
        product_id = int(request.data.get('productid'))
        product = get_object_or_404(Product,id=product_id)
        basket.add(product)
        return Response("added successfully")
    
    elif request.data.get('action') == 'delete':
        basket = Basket(request)
        print("deleting")
        print(request.data)
        product_id = int(request.data.get('productid'))
        basket.delete(product_id)

        return Response("deleted successfully")
