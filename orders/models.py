from django.db import models

# Create your models here.
class Customer(models.Model):
	fname = models.CharField('First Name', max_length=20)
	lname = models.CharField('Last Name', max_length=20)
	email = models.EmailField('Email Address')
	address = models.CharField('Address', max_length=20)
	street = models.CharField('Street', max_length=20)
	pincode = models.CharField('Pincode', max_length=10)
	gender = models.CharField('Gender', max_length=10)
	phone_no = models.IntegerField('Phone Number', max_length=10)
	allergy = models.CharField('Allergies', max_length=100)

	def __str__(self):
		return self.fname + ' ' + self.lname 

class Cuisine(models.Model):
	cuisine_name = models.CharField('Cuisine', max_length=20)

	def __str__(self):
		return self.cuisine_name

class Employee(models.Model):
	fname = models.CharField('First Name', max_length=20)
	lname = models.CharField('Last Name', max_length=20)
	email = models.EmailField('Email Address')
	address = models.CharField('Address', max_length=20)
	gender = models.CharField('Gender', max_length=10)
	phone_no = models.IntegerField('Phone Number', max_length=10)
	salary = models.IntegerField('Salary', max_length=10)

	def __str__(self):
		return self.fname + ' ' + self.lname 

class Chef(models.Model):
	chef_name = models.CharField('Chef Name', max_length=20)
	special = models.ForeignKey(Cuisine, blank=True, on_delete=models.CASCADE)
	emp_id = models.ForeignKey(Employee, blank=True, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.chef_name


class Ingredient(models.Model):
	ing_name = models.CharField('Ingredient Name', max_length=20)

	def __str__(self):
		return self.ing_name 

class Food(models.Model):
	food_name = models.CharField('Food Name', max_length=20)
	price = models.IntegerField('Price', max_length=5)
	quantity = models.IntegerField('Quantity', max_length=5)
	cuisineid = models.ForeignKey(Cuisine, blank=True, on_delete=models.CASCADE)
	ing_id = models.ManyToManyField(Ingredient, blank=True)
	chef_id = models.ForeignKey(Chef, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.food_name

class Drink(models.Model):
	drink_name = models.CharField('Drink Name', max_length=20)
	price = models.IntegerField('Price', max_length=5)
	quantity = models.IntegerField('Quantity', max_length=5)

	def __str__(self):
		return self.drink_name

class Delivery(models.Model):
	del_name = models.CharField('Delivery Name', max_length=20)
	vehicle_no = models.IntegerField(max_length=10)
	cust_id = models.ForeignKey(Customer, blank=True, on_delete=models.CASCADE)
	emp_id = models.ForeignKey(Employee, blank=True, on_delete=models.CASCADE)
	del_charge = models.IntegerField('Delivery Charge', max_length=5)
	del_time = models.DateTimeField('Delivery Time')

	def __str__(self):
		return self.del_name

class Order(models.Model):
	total_cost = models.IntegerField('Cost', max_length=10)
	food_id = models.ForeignKey(Food, blank=True, on_delete=models.CASCADE)
	drink_id = models.ForeignKey(Drink, blank=True, on_delete=models.CASCADE)


class Payment(models.Model):
	pay_method = models.CharField('Payment Method', max_length=20)
	cust_id = models.ForeignKey(Customer, blank=True, on_delete=models.CASCADE)
	order_id = models.ForeignKey(Order, blank=True, on_delete=models.CASCADE)


