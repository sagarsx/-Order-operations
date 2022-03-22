from itertools import product
from urllib import request
from django.shortcuts import render, redirect
from .forms import CustomerForm, OrderForm, ProductForm
from .models import *

# Create your views here.

def home(request):
    orders = Order.objects.all()
    context = {'orders':orders}
    return render(request, 'app/home.html', context)


def add_order(request):
    customer = Customer.objects.all()
    product = Product.objects.all()

    if request.method == "POST":
        print(request.POST)
        customer_name = request.POST["cust"]
        product_name = request.POST["prod"]
        price = request.POST["price"]
        qty = request.POST["qty"]
        total = request.POST["total"]  
        Order.objects.create(unit_price = price, quantity=qty, total_price=total, customer_id_id=customer_name, product_id_id=product_name)
        return redirect('/')
        # a = Customer.objects.get(id = customer_name)
        # b = Product.objects.get(id = product_name)
        # print(a)
        # print(b)
        # Order.objects.create(unit_price = price, quantity=qty, total_price=total, customer_id=Customer(id=customer_name), product_id=Product(id=product_name))
    context = {'customer':customer, 'product':product}
    return render(request, 'app/order.html', context)

    # customer = request.POST.get(customer_id=pk)
    # product = request.POST.get(product_id=pk)
    # price = request.POST.get(unit_price=pk)
    # qty = request.POST.get(quantity=pk)
    # total = request.POST.get(total_price=pk)  
    
    # if request.method == 'POST':
    #     form = OrderForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    # else:
    #     form = OrderForm
    # context = {'form':form}
    # return render(request, 'app/order.html', context)

def delete_order(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'order':order}
    return render(request, 'app/delete.html', context)

def edit_order(request, pk):
    customer = Customer.objects.all()
    product = Product.objects.get("id")
    order = Order.objects.get(id=pk)
    print(customer)

    if request.method == "POST":
        print(request.POST)
        customer_name = request.POST["cust"]
        product_name = request.POST["prod"]
        price = request.POST["price"]
        qty = request.POST["qty"]
        total = request.POST["total"]
        Order.objects.create(unit_price = price, quantity=qty, total_price=total, customer_id_id=customer_name, product_id_id=product_name)
        return redirect('/')

    # form = OrderForm(instance=order)
    # if request.method == "POST":
    #     form = OrderForm(request.POST, instance=order)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    
    # context = {'form':form}
    context = {'customer':customer, 'product':product, 'order':order}
    return render(request, 'app/edit.html')
