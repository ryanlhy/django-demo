"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.views import EmployeeView, EmployeeCreateView, UpdateEmployeeView, DeleteEmployeeView
from api.views import PokemonView, TestView, EbayView, CardSetsView, TestParamView, TestView2, CustomerView, CartView, CartDetailsView, OrderDetailsView
from api.views import OrdersView, OrdersCreateView
from rest.views import EmployeeViewSet, RegisterUsersView
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()

router.register(r'rest/employees', EmployeeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), # using rest_framework
    # employees
    path('employees/', EmployeeView.as_view()), # using default django view
    path('employees/create/', EmployeeCreateView.as_view()),
    path('employees/<int:employee_id>/', UpdateEmployeeView.as_view(), name='employee-update'),
    path('employees/<int:employee_id>/', DeleteEmployeeView.as_view(), name='employee-delete'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/signup/', RegisterUsersView.as_view(), name="user-signup"),
    path('pokemon/<path:param>/', PokemonView.as_view()), # using default pokemon api
    path('ebay/<path:param>/', EbayView.as_view()), # using default pokemon api
    #check all tables
    path('customer/', CustomerView.as_view()), 
    path('cart/', CartView.as_view()), 
    path('cartdetails/', CartDetailsView.as_view()), 
    path('orders/', OrdersView.as_view()), 
    path('orderdetails/', OrderDetailsView.as_view()), 
    #for testing
    path('set/', CardSetsView.as_view()), # testview for testing
    path('test/', TestView.as_view()), # testview for testing
    path('test2/', TestView2.as_view()), # testview2 for testing
    path('testparam/<path:param>/', TestParamView.as_view()), # test parameters view for testing
]
