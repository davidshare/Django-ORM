from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products, name='products'),
    path('customers/', views.customers, name='customers'),
    path('customers/<str:pk>/', views.customer, name='customer'),
]
