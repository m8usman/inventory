from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('product/<str:pk>/', views.product, name="product"),

    path('create-product/', views.createProduct, name="create-product"),

    path('update-product/<str:pk>/', views.updateProduct, name="update-product"),

    path('delete-product/<str:pk>/', views.deleteProduct, name="delete-product"),
]
