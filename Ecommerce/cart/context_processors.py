
from cart.models import Cart

def counter(request):
    item_count=0
    if request.user.is_authenticated:
        user=request.user
        try:
            cart=Cart.objects.filter(user=user)
            for i in cart:                     # taking each cart item
                item_count+=i.quantity

        except Cart.DoesNotExist:
            item_count=0
    return {'item_count':item_count}




