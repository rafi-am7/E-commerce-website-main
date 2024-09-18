from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        CartItems=order.get_cart_items
    else:
        CartItems=order['get_cart_items']
        order={'get_cart_items':0,'get_card_total':0,'shipping':False}
        items=[]
    products=Product.objects.all()
    context={'products':products,'CartItems':CartItems}
    return render(request,'myhtmls/store.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        CartItems=order.get_cart_items
    else:
        items=[]
        CartItems=order['get_cart_items']
        order={'get_cart_items':0,'get_card_total':0,'shipping':False}
    context={'items':items,'order':order,'CartItems':CartItems}
    
    return render(request,'myhtmls/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        CartItems=order.get_cart_items
    else:
        items=[]
        CartItems=order['get_cart_items']
        order={'get_cart_items':0,'get_card_total':0,'shipping':False}
    context={'items':items,'order':order,'CartItems':CartItems}
    return render(request,'myhtmls/checkout.html',context)

def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print(productId)
    print(action)
    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,created=OrderItem.objects.get_or_create(order=order,product=product)
    if action=='add':
        orderItem.quantity=orderItem.quantity+1
    elif action=='remove':
        orderItem.quantity=orderItem.quantity-1
    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()
        
    return JsonResponse('item added',safe=False)
