from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import OrderForm
from xhtml2pdf import pisa
# Create your views here.
from .models import Product,Order
from .cart import Cart
def home(request):
    if request.session.get('cart'):
        x=list(request.session.get('cart').keys())
        print(Product.objects.get(id=int(x[0])))
   #     pass
    form=Product.objects.all()
    f=OrderForm()

    '''
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Added suuccesfully")
        else:
            form.save()
            return HttpResponse("Invalid credentials")'''
    return render(request,'home.html',context={'form':form,'f':f})

def add(request):
    '''if request.method=="POST":
        file=request.POST['file']
        o=Order(order_data=file,order_completed=True)
        o.save()
        return HttpResponse("success")'''
    form=OrderForm(request.POST)
    form.save()


def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")



def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")



def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")



def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def cart_detail(request):
    print(request.POST)
    print(request.session.get('cart'))
    return render(request, 'cart.html')
    
def hf(request,category):
    p=Product.objects.filter(product_sub_category=category)
    return render(request,'hf.html',context={'f':p})
    


def addtobase(request):
    if request.method=='POST':
        if request.session.get('cart'):
            x=list(request.session.get('cart').keys())
            print(x)
            for i in x:
                print("i:",i)
                p=Product.objects.get(id=int(i))
                o=Order(product=p,customer_name=request.POST['firstname'],customer_email=request.POST['email'],customer_number=request.POST['city'],customer_address=request.POST['address'],order_completed=False)
                o.save()
            return HttpResponse("success!!")


def detail(request,id):
    product=Product.objects.get(id=id)
    return render(request,'detail.html',context={'product':product})