from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views import View 
from model.models import Employee, CardSets, TestTable, Customer, Cart, CartDetails, Orders, OrderDetails
from django.core.serializers import serialize
from .helpers import GetBody
from django.forms.models import model_to_dict
import json
from services.poke_api_services import get_data_from_api
from services.ebay_api_services import get_data_from_ebay_api
# from services.ebay_api_services import handle_negative_keywords
from utils.ebay_data_manipulation import handle_negative_keywords, main_response_data_handler
from django.db.models import Field

# Get a list of all the fields in the Employee model
employee_fields = Employee._meta.get_fields()
# Filter out the fields that are not columns
column_names = [field.name for field in employee_fields if isinstance(field, Field)]

class EmployeeView(View):
    def get(self, request):
        all_employees = Employee.objects.all()
        return JsonResponse(json.loads(serialize("json", all_employees)), safe=False)

class EmployeeCreateView(View):
    def post(self, request):
        body = GetBody(request)
        employee = Employee(name=body["name"], job_title=body["job_title"], income=body["income"])
        employee.save()
        return JsonResponse(json.loads(json.dumps(model_to_dict(employee))), safe=False)

class UpdateEmployeeView(View):
    def put(self, request, employee_id):
        if request.method == 'PUT':
            try:
                employee = Employee.objects.get(id=employee_id)
                body = json.loads(request.body)
                for column_name in column_names:
                    setattr(employee, column_name, body.get(column_name, getattr(employee, column_name)))
                employee.save()
                return JsonResponse({'success': True})
            except Employee.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Employee not found'}, status=404)
        else:
            return HttpResponseNotAllowed(['PUT'])

class DeleteEmployeeView(View):
    def delete(self, request, employee_id):
        try:
            employee = Employee.objects.get(id=employee_id)
            employee.delete()
            return HttpResponse(status=204)
        except Employee.DoesNotExist:
            return HttpResponse(status=404) 
        
class PokemonView(View):
    def get(self, request, param):
        query = request.GET.get("query", "no query") ## Grab query from url query
        data = get_data_from_api(param)
        return JsonResponse({"param": param, "query": query, "data": data["data"]})

class EbayView(View):
    def get(self, request, param):
        query = request.GET.get("query", "no query") ## Grab query from url query
        param = json.loads(param)
        # data1 = get_data_from_ebay_api(param["search"])
        # negative_keywords = handle_negative_keywords("cgc", data)
        data = main_response_data_handler(param)
        return JsonResponse({"param": param, "query": query, "data": data["ebayData"], "filterCalls": data["filterCalls"] })

class CardSetsView(View):
    def get(self, request):
        card_sets = CardSets.objects.all()
        return JsonResponse(json.loads(serialize("json", card_sets)), safe=False)
# check all tables
class CustomerView(View):
    def get(self, request):
        customers = Customer.objects.all()
        return JsonResponse(json.loads(serialize("json", customers)), safe=False)

class CartView(View):
    def get(self, request):
        carts = Cart.objects.all()
        return JsonResponse(json.loads(serialize("json", carts)), safe=False)

class CartDetailsView(View):
    def get(self, request):
        cart_details = CartDetails.objects.all()
        return JsonResponse(json.loads(serialize("json", cart_details)), safe=False)

class OrdersView(View):
    def get(self, request):
        orders = Orders.objects.all()
        return JsonResponse(json.loads(serialize("json", orders)), safe=False)

    def post(self, request):
        body = GetBody(request)
        orders = Orders(customer=body["customer"], total=body["total"], date_created=body["date_created"], notes=body["notes"])
        orders.save()        

        return JsonResponse(json.loads(json.dumps(model_to_dict(employee))), safe=False)

class OrderDetailsView(View):
    def get(self, request):
        order_details = OrderDetails.objects.all()
        return JsonResponse(json.loads(serialize("json", order_details)), safe=False)
        
class TestView(View):
    def get(self, request):
        card_sets = CardSets.objects.all()
        # param = serialize("json", card_sets1)
        return JsonResponse({"message": "Hello, world! Test worked","card":json.loads(serialize("json", card_sets))})
        # return JsonResponse(json.loads(serialize("json", card_sets1)), safe=False)
        # return JsonResponse({"message":"param"})

class TestView2(View):
    def get(self, request):
        test_view2 = TestTable.objects.all()
        return JsonResponse({"message": "Hello, world! Test worked","card":json.loads(serialize("json", test_view2))})
 
    def post(self, request):
        body = GetBody(request)
        test = TestTable(name=body["name"])
        test.save()        
        
        return JsonResponse(json.loads(json.dumps(model_to_dict(test))), safe=False)

class TestParamView(View):
    def get(self, request, param):
        # print(param)
        param_decode = json.loads(param)
        # param = serialize("json", param)
        return JsonResponse({"message":param_decode})