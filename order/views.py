import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from order.models import Customer, Order, OrderItems, Product
from django.contrib.auth.decorators import login_required
# Create your views here.


##showing all the items on the main screen
@login_required
def index(request):
    products = Product.objects.all()
    return render(request, "index.html",{"products": products})

#Authentication for logging in
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            alert = True
            return render(request, "login.html",{"alert":alert})
    return render(request,"login.html")

def Logout(request):
    logout(request)
    alert = True
    return render(request,"index.html",{'alert':alert})

##Register new user
def register(request):
    if request.method=="POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        user = User.objects.create_user(username=username, password=password1,email=email)
        customers = Customer.objects.create(user=user, phone_number=phone_number)
        user.save()
        customers.save()
        return render(request,"login.html")
    return render(request,'register.html') 

##Customers are able to add to cart
@login_required
def addItem(request):
    data = json.loads(request.body)
    itemid = data['id']
    
    customer = request.user.customer
    product = Product.objects.get(id=itemid)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItems.objects.get_or_create(order=order, product=product)
    
    product.quantity_in_stock = (product.quantity_in_stock - 1)
    product.save()
    orderItem.save()
    
    if orderItem.quantity_in_stock <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

## initial setup for items in cart for a logged in user
@login_required
def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    return {'cartItems':cartItems, 'items':items, 'order':order}



##history of the orders
@login_required
def history(request):
    history = Order.objects.filter(Customer = request.user)
    context = {
            'history':history
        }
    return render(request, "order_history.html",context)