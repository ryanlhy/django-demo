from django.shortcuts import render
from model.models import Employee, Customer, Cart, TestTable, CartDetails
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .serializers import EmployeeSerializer, UserSerializer, CustomerSerializer, CartSerializer, TestTableSerializer, CartDetailsSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated] # Could be [permissions.IsAuthenticated]

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetailsViewSet(viewsets.ModelViewSet):
    queryset = CartDetails.objects.all()
    serializer_class = CartDetailsSerializer

    def get_queryset(self): # filter by cart_id
        queryset = super().get_queryset()
        cart_id = self.request.query_params.get('cart_id', None)
        if cart_id is not None:
            queryset = queryset.filter(cart=cart_id)
        return queryset

class TestTableViewSet(viewsets.ModelViewSet):
    queryset = TestTable.objects.all()
    serializer_class = TestTableSerializer

class RegisterUsersView(generics.ListCreateAPIView):
    """
    POST user/signup/
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username or not password or not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        # Serialize the new user object and include it in the response
        # serializer = UserSerializer(new_user)
        return Response(status=status.HTTP_201_CREATED)
        # return Response(data=new_user, status=status.HTTP_201_CREATED)