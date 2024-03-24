# application/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    # Ajoutez d'autres URLs pour les vues supplémentaires
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('category/new/', views.category_form, name='category_form'),
    path('product/new/', views.product_form, name='product_form'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
]
