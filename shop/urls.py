from django.urls import path
from . import views

app_name= 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.product_list, name='product_list'),
    path('catalog/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('catalog/detail/<int:id>/<slug:slug>/', views.product_detail,  name='product_detail'),
    path('about/', views.about, name='about_us'),
    path('contact/', views.contact, name='contact'),
]