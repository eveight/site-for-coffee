from django.urls import path
from coffee_shop import views

urlpatterns = [
    path('', views.coffee_shop_view, name='coffee'),
    path('position', views.position_view, name='position_view'),
    path('add-session-view/<int:id>', views.add_session_view, name='add_session_view'),
    path('order-view', views.order_view, name='order_view'),
    path('delete-session-view', views.delete_session_view, name='delete_session_view'),
    path('delete-value-session-order-view/<int:id>', views.delete_value_session_order_view,
         name='delete_value_session_order_view'),
    path('create-order-view', views.create_order_view, name='create_order_view'),
    path('order-list-view', views.order_list_view, name='order_list_view'),

    # RestAPI
    path('api/positions', views.PositionListView.as_view()),
    path('api/orders', views.OrderListView.as_view()),
    path('api/create-position', views.PositionCreateView.as_view()),
    path('api/create-order', views.OrderCreateView.as_view()),
    path('api/rud-position/<int:pk>', views.PositionRetrieveUpdateDestroy.as_view()),
    path('api/rud-order/<int:pk>', views.OrderRetrieveUpdateDestroy.as_view()),

]
