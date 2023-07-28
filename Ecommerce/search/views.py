from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

from django.http import HttpResponse
# Create your views here.

# VIEW TO SEARCH  PRODUCTS
def searchresult(request):
    products=None  # while searching prods, if we are not giving any keywords and click, it will shows Prod as "None"
    if request.method=="POST":
        query=request.POST.get('q') # getting the keyword here
        if query:
            products=Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'search.html',{'query':query,'products':products})


# filter =to get only some elements
# Q object is used to create complex queries by combining multiple conditions with logical operators.

