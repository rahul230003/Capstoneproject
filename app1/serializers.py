from .models import BookingTable,MenuTable
from rest_framework import serializers
from django.contrib.auth.models import User

class MenuTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuTable
        fields = '__all__'

class BookingTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ['url', 'username', 'email', 'groups']
