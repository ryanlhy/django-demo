from django.shortcuts import render
from django.http import JsonResponse
from django.views import View 
from model.models import Employee, CardSets
from django.core.serializers import serialize
from .helpers import GetBody
from django.forms.models import model_to_dict
import json
from services.services_tcg import get_data_from_api
from services.ebay_api_services import get_data_from_ebay_api
# from services.ebay_api_services import handle_negative_keywords
from utils.ebay_data_manipulation import handle_negative_keywords

class EmployeeView(View):
    def get(self, request):
        all_employees = Employee.objects.all()
        return JsonResponse(json.loads(serialize("json", all_employees)), safe=False)

    def post(self, request):
        body = GetBody(request)
        employee = Employee(name=body["name"], job_title=body["job_title"], income=body["income"])
        employee.save()        
        
        return JsonResponse(json.loads(json.dumps(model_to_dict(employee))), safe=False)
        
class PokemonView(View):
    def get(self, request, param):
        query = request.GET.get("query", "no query") ## Grab query from url query
        data = get_data_from_api(param)
        return JsonResponse({"param": param, "query": query, "data": data})

class EbayView(View):
    def get(self, request, param):
        query = request.GET.get("query", "no query") ## Grab query from url query
        data = get_data_from_ebay_api(param)
        negative_keywords = handle_negative_keywords("cgc", data)
        return JsonResponse({"param": param, "query": query, "data": data, "negative_keywords_index": negative_keywords})

class CardSetsView(View):
    def get(self, request):
        card_sets = CardSets.objects.all()
        return JsonResponse(json.loads(serialize("json", card_sets)), safe=False)

class TestView(View):
    def get(self, request):
        return JsonResponse({"message": "Hello, world! Test worked"})
    
