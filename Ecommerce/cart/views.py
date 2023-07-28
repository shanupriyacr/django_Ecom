from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from shop.models import Product
from cart.models import Cart

from cart.models import Cart,Account,Order
from django.shortcuts import redirect

from django.contrib import messages
from django.http import HttpResponse

from django.shortcuts import render
from .models import Cart, Account, Order

# VIEW FOR CART (view connects to cart.html)

@login_required
def cart_view(request):
     total=0
     try:
          user=request.user
          cart=Cart.objects.filter(user=user)
          for i in cart:                        # i= each cart object
               total+=i.quantity * i.products.price
     except Cart.DoesNotExist:                  # if the object is not there
          pass
     return render(request,'cart.html',{'cart':cart,'total':total})


# VIEW FOR ADD TO CART

@login_required
def add_cart(request,p):
     product=Product.objects.get(id=p)           # product detail of particular product "p" to be added
     user=request.user                          # user info
     try:
          cart=Cart.objects.get(products=product,user=user) # if same "prod & user" (object) is there
          if cart.quantity < cart.products.stock:
               cart.quantity+=1
          cart.save()
     except Cart.DoesNotExist:
          cart=Cart.objects.create(products=product,user=user,quantity=1)
          cart.save()

     return redirect('cart:cart_view')


# @login_required =decorator is used in Django to restrict access to a view function only authenticated users.
# render = connect to "html"
# redirect= to connect to "view"


# VIEW FOR "-" IN  CART

@login_required
def cart_remove(request,p):
     user = request.user
     product = Product.objects.get(id=p)
     try:
          cart = Cart.objects.get(products=product, user=user)
          if cart.quantity > 1:
               cart.quantity-=1
               cart.save()
          else:
               cart.delete()

     except:
          pass
     return redirect('cart:cart_view')


#quantity=0 , means, entire row will get deleted


# VIEW FOR "full_remove/trash" IN  CART

@login_required
def full_remove(request,p):
     user = request.user
     product = Product.objects.get(id=p)
     try:
          cart = Cart.objects.get(products=product, user=user)
          cart.delete()
     except:
          pass

     return redirect('cart:cart_view')



# VIEW FOR "orderform/place order" IN  CART
# (get values of -->Address,Ph_no,Acct_no )

@login_required
def order(request):
     total=0
     items=0
     msg=0
     if(request.method=="POST"):
          a=request.POST['a']
          p=request.POST['p']
          num=request.POST['num']
          user=request.user
          cart=Cart.objects.filter(user=user)

          for i in cart:
               total+=i.quantity*i.products.price
               items+=i.quantity
          ac=Account.objects.get(acctnumber=num)
          if float(ac.amount) >= total:
                    ac.amount=ac.amount - total
                    ac.save()
                    for i in cart:             # to add details to Order table
                         o=Order(user=user,products=i.products,address=a,phone=p,order_status="paid",noofitems=i.quantity)
                         o.save()
                    cart.delete()
                    msg="Order Placed Successfully"
                    return render(request,'orderdetail.html',{'msg':msg,'total':total,'items':items})
          else:
                    msg = "Insufficent Amount.You can't Place Order"
                    return render(request, 'orderdetail.html',{'msg':msg})

     return render(request,'orderform.html')


# try = if exception comes, it will prevent from stop checking whether an object is present/not
#  p --> p= total_amt in the cart, a.amount= amt already have
# a.amount=a.amount -p      --> updated the new amount in a.amount

# to find number of items(quantity)



# VIEW FOR "orderview" IN  CART


@login_required
def orderview(request):
     user=request.user
     o=Order.objects.filter(user=user,order_status="paid")
     return render(request,'orderview.html',{'o':o,'name':user.username})