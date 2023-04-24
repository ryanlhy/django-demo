from model.models import Employee, Customer, Cart, TestTable, CartDetails
from rest_framework import serializers
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'job_title', 'income']

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'address', 'uid', 'signup_date', 'signin_date','is_active']

class CartSerializer(serializers.HyperlinkedModelSerializer):
    # Customer model that is related to an Order model
    # customer = serializers.HyperlinkedRelatedField(view_name='customer-detail', read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'customer', 'total', 'last_updated', 'notes']

class CartDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartDetails
        fields = ['id', 'cart', 'ebay_item_number', 'bid_amount', 'name', 'pokemon_id', 'grade', 'date_added']

class TestTableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestTable
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)