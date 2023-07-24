from django.urls import path
from .views import HomeView, ProductListView, ProductDetailsView, CategoryListView
urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("products-list", ProductListView.as_view(), name="product-list"),
    path("product-detail/<int:id>",ProductDetailsView.as_view(), name="product-detail" ),
    path("categories", CategoryListView.as_view(), name="category-list" )
]