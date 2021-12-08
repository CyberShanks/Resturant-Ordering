from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('chefs', views.all_chef, name="list_chef"),
    path('customers', views.all_cus, name="list_cus"),
    path('menu', views.menu, name="menu"),

]
