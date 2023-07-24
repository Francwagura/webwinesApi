from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

# restframework & serializers
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from.serializers import ProductListSerializer, ProductDetailSerializer, CategoryListSerializer
# Create your views here.

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




