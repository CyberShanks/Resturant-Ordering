from django.contrib import admin
from .models import Customer 
from .models import Cuisine
from .models import Employee 
from .models import Chef 
from .models import Ingredient 
from .models import Food
from .models import Drink 
from .models import Delivery
from .models import Order 
from .models import Payment

# Register your models here.
admin.site.register(Customer)
admin.site.register(Cuisine)
admin.site.register(Employee)
admin.site.register(Chef)
admin.site.register(Ingredient)
admin.site.register(Food)
admin.site.register(Drink)
admin.site.register(Delivery)
admin.site.register(Order)
admin.site.register(Payment)