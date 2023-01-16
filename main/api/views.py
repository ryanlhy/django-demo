from django.shortcuts import render
from django.http import JsonResponse
from django.views import View 
from model.models import Employee
from django.core.serializers import serialize
from .helpers import GetBody
import json

class EmployeeView(View):
    def get(self, request):
        result = json.loads(serialize("json", Employee.objects.all()))
        return JsonResponse(result, safe=False)

    def post(self, request):
        body = GetBody(request)
        created = Employee.objects.create(name=body["name"], job_title=body["job_title"], income=body["income"])
        print("Created", type(created))
        return JsonResponse(json.loads(serialize("json", [created])), safe=False)
        
        
    
