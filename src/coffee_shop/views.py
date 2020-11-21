import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from coffee_shop.forms import OrderForms
from .models import Category, Position, Order

from rest_framework import generics
from .serializers import PositionListSerializer
from .serializers import OrderListSerializer


@login_required(login_url='accounts/login')
def coffee_shop_view(request):
    order_count = count_order_view(request)
    all_category = Category.objects.all()
    return render(request, 'coffee_shop/coffee.html', {'order_count': order_count,
                                                       'all_category': all_category})


@login_required(login_url='accounts/login')
def position_view(request):
    order_count = count_order_view(request)
    category_id = request.GET['category_id']
    all_position = Position.objects.filter(category=category_id)
    return render(request, 'coffee_shop/position.html', {'order_count': order_count,
                                                         'all_position': all_position})


def add_session_view(request, id):
    if 'product_id' not in request.session:
        request.session['product_id'] = list()
    request.session['product_id'].append(int(id))
    request.session.modified = True
    return redirect('/')


def delete_session_view(request):
    if 'product_id' in request.session:
        del request.session['product_id']
    return redirect('/')


def order_view(request):
    if 'product_id' in request.session and len(request.session['product_id']) > 0:
        order_details = []
        for id in request.session['product_id']:
            order_details.append(Position.objects.filter(id=id))

        all_order_sum = 0
        for obj_list in order_details:
            for obj in obj_list:
                all_order_sum += obj.price
        request.session['all_order_sum'] = all_order_sum

        client_sum = OrderForms()
    else:
        return redirect('/')
    return render(request, 'coffee_shop/order_details.html', {'order_details': order_details,
                                                              'client_sum': client_sum,
                                                              'all_order_sum': all_order_sum})


def create_order_view(request):
    if request.method == "POST":
        position_id = request.session['product_id']
        client_sum = int(request.POST['in_sum']) - request.session['all_order_sum']
        new_order = Order.objects.create(seller=request.user, time=datetime.datetime.now(), position_id=position_id,
                                         price=request.session['all_order_sum'])
        del request.session['product_id']
        del request.session['all_order_sum']
        messages.success(request, 'Заказ № {}, продавец {}, сдача - {} грн'.format(new_order.id, new_order.seller,
                                                                                   client_sum))
    return redirect('/')


def delete_value_session_order_view(request, id):
    request.session['product_id'].remove(id)
    request.session.modified = True
    return redirect(order_view)


def count_order_view(request):
    if 'product_id' in request.session:
        order_count = len(request.session['product_id'])
    else:
        order_count = 0
    return order_count


def order_list_view(request):
    today_month = datetime.date.today().month
    all_order_in_this_month = Order.objects.filter(time__month=today_month).order_by('-time')

    order_with_position = {}
    for obj in all_order_in_this_month:
        all_position = Position.objects.filter(id__in=obj.position_id)
        order_with_position[obj] = all_position
    return render(request, 'coffee_shop/order_list.html', {'qs': order_with_position})


class PositionListView(generics.ListAPIView):
    """ API list positions"""
    queryset = Position.objects.all()
    serializer_class = PositionListSerializer


class OrderListView(generics.ListAPIView):
    """ API list orders"""
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class PositionCreateView(generics.CreateAPIView):
    """ API create position"""
    serializer_class = PositionListSerializer


class OrderCreateView(generics.CreateAPIView):
    """ API create order"""
    serializer_class = OrderListSerializer


class PositionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """ API retrieve update destroy position"""
    queryset = Position.objects.all()
    serializer_class = PositionListSerializer
