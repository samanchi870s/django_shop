from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


# Create your views here.
def index_page(request):
    category = models.Category.objects.all()
    products = models.Product.objects.all()

    return render(request, 'index.html', {'category':category, 'product': products})

# Получить товары из конкретной котегори
def get_category(request, pk):
    current_category = models.Category.objects.get(id=pk)
    get_current_category_products = models.Product.objects.filter(product_category=current_category)
    return render(request, 'category_product.html', {'products': get_current_category_products})

def searcuh_product(request):
    if request.method == 'POST':
        current_product =request.POST.get("saerch")
        try:
            get_product = models.POST.odject.get(product_name=current_product)

            return render(request, 'current_product.html', {'product': get_product})
        except:
            return  redirect('/')

# ПОлучить коркретный продукт
def get_product(request, pk):
    current_product = models.Product.objects.get(id=pk)

    return render(request, 'current_product.html', {'product': current_product})
def create_cart(request, pk):
    product = models.Product.objects.get(id=pk)
    if request.method =="POST":
        product_count = request.POST.get('counter')

        cart = models.UserCart(user_id=request.user.id, product=product, quantity=product_count)
        cart.save()

        return redirect('/')

def get_user_cart(request):
    user_cart = models.UserCart.objects.filter(user_id=request.user.id)
    total = sum([ i.product.product_price*i.quantity for i in user_cart])

    return render(request, 'user_cart.html', {'cart': user_cart, 'total': total})



def about(request):
    return HttpResponse('About us')


def products(request):
    return HttpResponse('All products')
