from .models import Position, Order
from rest_framework import serializers


class PositionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


