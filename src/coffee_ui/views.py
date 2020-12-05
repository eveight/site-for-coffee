from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests

from coffee_ui.forms import FormPosition, FormOrder, DeleteAPI


def ui_choose(request):
    return render(request, 'coffee_ui/ui_choose.html')


def read_rest_api(request):
    r = requests.get('http://127.0.0.1:8000/api/positions')
    body = r.json()

    return render(request, 'coffee_ui/ui_positions.html', {'data': body})


def create_position_api(request):
    form = FormPosition()
    if request.method == 'POST':
        form = FormPosition(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            category = form.cleaned_data['category']

            r = requests.post('http://127.0.0.1:8000/api/create-position', data={
                'name': name,
                'price': price,
                'category': category,
            })

            if r.status_code == 201:
                return redirect(read_rest_api)

    return render(request, 'coffee_ui/ui_create_position.html', {'form': form})


def read_rest_api_orders(request):
    r = requests.get('http://127.0.0.1:8000/api/orders')
    body = r.json()

    return render(request, 'coffee_ui/ui_orders.html', {'data': body})


def create_orders_api(request):
    form = FormOrder()
    if request.method == 'POST':
        form = FormOrder(request.POST)
        if form.is_valid():
            time = form.cleaned_data['time']
            position_id = form.cleaned_data['position_id']
            position_id = '[' + position_id + ']'
            price = form.cleaned_data['price']
            seller = form.cleaned_data['seller']

            r = requests.post('http://127.0.0.1:8000/api/create-order', data={
                'time': time,
                'position_id': position_id,
                'price': price,
                'seller': seller,
            })

            if r.status_code == 201:
                return redirect(read_rest_api_orders)

    return render(request, 'coffee_ui/ui_create_order.html', {'form': form})


def delete_position_api(request):
    form = DeleteAPI()
    if request.method == "POST":
        form = DeleteAPI(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']

            r = requests.delete('http://127.0.0.1:8000/api/rud-position/{}'.format(id))

            if r.status_code == 204:
                return redirect(ui_choose)
    return render(request, 'coffee_ui/ui_delete_position.html', {'form': form})


def delete_order_api(request):
    form = DeleteAPI()
    if request.method == "POST":
        form = DeleteAPI(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']

            r = requests.delete('http://127.0.0.1:8000/api/rud-order/{}'.format(id))

            if r.status_code == 204:
                return redirect(ui_choose)
    return render(request, 'coffee_ui/ui_delete_order.html', {'form': form})


def put_position_api(request):
    form = FormPosition()
    form_id = DeleteAPI()
    if request.method == 'POST':
        form = FormPosition(request.POST)
        form_id = DeleteAPI(request.POST)
        if form.is_valid() and form_id.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            category = form.cleaned_data['category']
            id = form_id.cleaned_data['id']

            r = requests.put('http://127.0.0.1:8000/api/rud-position/{}'.format(id),
                             data={'id': id,
                                   'name': name,
                                   'price': price,
                                   'category': category})

            if r.status_code == 200:
                return redirect(ui_choose)
    return render(request, 'coffee_ui/put_position.html', {'form': form, 'form_id': form_id})


def put_order_api(request):
    form = FormOrder()
    form_id = DeleteAPI()
    if request.method == 'POST':
        form = FormOrder(request.POST)
        form_id = DeleteAPI(request.POST)
        if form.is_valid() and form_id.is_valid():
            time = form.cleaned_data['time']
            position_id = form.cleaned_data['position_id']
            position_id = '[' + position_id + ']'
            price = form.cleaned_data['price']
            seller = form.cleaned_data['seller']
            id = form_id.cleaned_data['id']

            r = requests.put('http://127.0.0.1:8000/api/rud-order/{}'.format(id),
                             data={'id': id,
                                   'time': time,
                                   'position_id': position_id,
                                   'price': price,
                                   'seller': seller})

            if r.status_code == 200:
                return redirect(ui_choose)
    return render(request, 'coffee_ui/put_order.html', {'form': form, 'form_id': form_id})
