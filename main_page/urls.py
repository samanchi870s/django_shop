from django.urls import path
from . import views

# Создаем адреса
urlpatterns = [
    path('', views.index_page),
    path('about', views.about),
    path('products', views.products),
    path('category/<int:pk>', views.get_category),
    path('search', views.searcuh_product),
    path('product/<int:pk>', views.get_product),
    path('add_to_cart/<int:pk>', views.create_cart),
    path('korzina', views.get_user_cart)


]


