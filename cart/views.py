from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Cotegory, Product, Cart



class HomeView(View):
    def get(self, request):
        product = Product.objects.filter(is_stock=True)
        count = Cart.objects.count()
        category = Cotegory.objects.all()
        return render(request, 'cart/home.html', {'product': product, 'count':count, 'category': category})

class CotegoryView(View):
    def get(self, request, id):
        category = Cotegory.objects.all()
        cotegory = get_object_or_404(Cotegory, id=id)
        product = cotegory.products.all()
        return render(request, 'cart/home.html', {'product':product, 'category': category})

class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        count = Cart.objects.count()
        category = Cotegory.objects.all()
        return render(request, 'cart/detail.html', {'product': product, 'count':count, 'category': category})


    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        quaintity = int(request.POST['cart'])
        if Cart.objects.filter(product=product).exists():
            cart = Cart.objects.filter(product=product).first()
            cart.quantity += quaintity
            cart.save()
        else:
            cart = Cart()
            cart.product = product
            cart.quantity = quaintity
            cart.save()
        return redirect('cart:home')


class CartDetailView(View):
    def get(self, request):
        product = Cart.objects.all()
        count = Cart.objects.count()
        category = Cotegory.objects.all()
        return render(request, 'cart/cart_detail.html', {'product': product, 'count':count, 'category': category})

def delete(request, delete_id):
    cart = get_object_or_404(Cart, id=delete_id)
    cart.delete()
    return redirect('cart:home')