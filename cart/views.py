from django.shortcuts import render
from .models import Cart
# Create your views here.
def cart_home(request):
	#del request.session['cart_id']
	cart_id	=	request.session.get("cart_id",None)
	if cart_id is None:
		cart_obj	=	Cart.objects.create(user=None)
		print('create new cart')
		request.session['cart_id'] = cart_obj.id
	else:
		print("Cart Id exists")
		print(cart_id)
		cart_obj=Cart.objects.get(id=cart_id)
	return render(request,"home1.html",{})