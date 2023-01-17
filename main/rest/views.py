from django.shortcuts import render
from model.models import Employee
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny] # Could be [permissions.IsAuthenticated]