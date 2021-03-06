# Generated by Django 4.0 on 2021-12-07 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chef_name', models.CharField(max_length=20, verbose_name='Chef Name')),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine_name', models.CharField(max_length=20, verbose_name='Cuisine')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20, verbose_name='First Name')),
                ('lname', models.CharField(max_length=20, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('address', models.CharField(max_length=20, verbose_name='Address')),
                ('street', models.CharField(max_length=20, verbose_name='Street')),
                ('pincode', models.CharField(max_length=10, verbose_name='Pincode')),
                ('gender', models.CharField(max_length=10, verbose_name='Gender')),
                ('phone_no', models.IntegerField(max_length=10, verbose_name='Phone Number')),
                ('allergy', models.CharField(max_length=100, verbose_name='Allergies')),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_name', models.CharField(max_length=20, verbose_name='Drink Name')),
                ('price', models.IntegerField(max_length=5, verbose_name='Price')),
                ('quantity', models.IntegerField(max_length=5, verbose_name='Quantity')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20, verbose_name='First Name')),
                ('lname', models.CharField(max_length=20, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('address', models.CharField(max_length=20, verbose_name='Address')),
                ('gender', models.CharField(max_length=10, verbose_name='Gender')),
                ('phone_no', models.IntegerField(max_length=10, verbose_name='Phone Number')),
                ('salary', models.IntegerField(max_length=10, verbose_name='Salary')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=20, verbose_name='Food Name')),
                ('price', models.IntegerField(max_length=5, verbose_name='Price')),
                ('quantity', models.IntegerField(max_length=5, verbose_name='Quantity')),
                ('chef_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.chef')),
                ('cuisineid', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.cuisine')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ing_name', models.CharField(max_length=20, verbose_name='Ingredient Name')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.IntegerField(max_length=10, verbose_name='Cost')),
                ('drink_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.drink')),
                ('food_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.food')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_method', models.CharField(max_length=20, verbose_name='Payment Method')),
                ('cust_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.customer')),
                ('order_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='ing_id',
            field=models.ManyToManyField(blank=True, to='orders.Ingredient'),
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('del_name', models.CharField(max_length=20, verbose_name='Delivery Name')),
                ('vehicle_no', models.IntegerField(max_length=10)),
                ('del_charge', models.IntegerField(max_length=5, verbose_name='Delivery Charge')),
                ('del_time', models.DateTimeField(verbose_name='Delivery Time')),
                ('cust_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.customer')),
                ('emp_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.employee')),
            ],
        ),
        migrations.AddField(
            model_name='chef',
            name='emp_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.employee'),
        ),
        migrations.AddField(
            model_name='chef',
            name='special',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.cuisine'),
        ),
    ]
