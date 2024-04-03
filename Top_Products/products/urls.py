from django.urls import path

from products import views

urlpatterns = [
    path('',views.Home),
    path('categories/<str:category_name>/products', views.top_products, name='top_products'),
    path('categories/<str:category_name>/products/<int:product_id>', views.product_details, name='product_details'),
]