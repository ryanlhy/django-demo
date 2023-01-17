from django.shortcuts import render
from django.http import JsonResponse
from django.views import View 
from model.models import Employee
from django.core.serializers import serialize
from .helpers import GetBody
import json

class EmployeeView(View):
    def get(self, request):
        all_employees = Employee.objects.all()
        result = json.loads(serialize("json", all_employees.filter(job_title = "Software Engineer")))
        return JsonResponse(result, safe=False)

    def post(self, request):
        body = GetBody(request)
        employee = Employee(name=body["name"], job_title=body["job_title"], income=body["income"])
        employee.save()
        print("Created", type(employee))
        return JsonResponse(json.loads(serialize("json", [employee])), safe=False)
        
        
    
