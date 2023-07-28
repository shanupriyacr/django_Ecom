from django.shortcuts import render
from shop.models import Category,Product

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

# Create your views here.

# VIEW TO DISPLAY ALL PRODUCTS CATEGORY
def allProdCat(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})

# VIEW TO ALL PRODUCTS
def allproducts(request,cslug):  # cslug= the slug value that passing
    c=Category.objects.get(slug=cslug)
    p=Product.objects.filter(category__slug=cslug)  # category__slug=the slug value of category (foreign key)
    return render(request,'products.html',{'p':p,'c':c})


# VIEW TO SEE A PARTICULAR  PRODUCTS
def prodetail(request,pslug):
    p=Product.objects.get(slug=pslug)
    return render(request,'detail.html',{'p':p})


# REGISTER VIEW
def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        p=request.POST['p']
        cp=request.POST['cp']
        if p==cp:
            user=User.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p)
            user.save()
            return user_login(request)
    return render(request,'register.html')


# LOGIN VIEW
def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p) # function inside 'auth'
        if user:
            login(request,user)
            return allProdCat(request)
        else:
            messages.error(request,"Invalid Credentials")

    return render(request, 'login.html')


# LOGIOUT VIEW
def user_logout(request):
    logout(request)
    return allProdCat(request)


