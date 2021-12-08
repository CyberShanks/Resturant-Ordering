from django.shortcuts import render
from datetime import datetime
from .models import Chef
from .models import Customer
from .models import Food
from .models import Drink

def home(request):
	current_year=datetime.now().year
	return render(request, 'home.html', {
		"current_year": current_year,
		})

def all_chef(request):
	chef_list = Chef.objects.all()
	return render(request, 'chef.html', {
		'chef_list' : chef_list,
		})

def all_cus(request):
	customer_list = Customer.objects.all()
	return render(request, 'customer.html', {
		'customer_list' : customer_list,
		})

def menu(request):
	food_list = Food.objects.all()
	drink_list = Drink.objects.all()
	return render(request, 'menu.html', {
		'food_list' : food_list,
		'drink_list' : drink_list,
		})