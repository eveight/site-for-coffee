from django.urls import path

from coffee_ui import views

urlpatterns = [
    path('', views.ui_choose),
    path('positions/', views.read_rest_api, name='read_rest_api'),
    path('orders/', views.read_rest_api_orders, name='read_rest_api_orders'),
    path('create-position/', views.create_position_api, name='create_position'),
    path('create-order/', views.create_orders_api, name='create_orders'),
    path('delete-position/', views.delete_position_api, name='delete_position_api'),
    path('delete-order/', views.delete_order_api, name='delete_order_api'),
    path('put-position/', views.put_position_api, name='put_position_api'),
    path('put-order-api/', views.put_order_api, name='put_order_api')
]