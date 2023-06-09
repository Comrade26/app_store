from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Vendor.models import Product, Category, Vendor
from Buyer.models import Order
from django.shortcuts import get_object_or_404
from django.views import View
from django.urls import reverse

def item(request):
    productID = request.GET.get("product")
    products = Product.get_products_by_id(productID)

    product_map = {}
    product_map["products"] = products

    return render(request, "single_products.html", product_map)

@login_required
def vendor_item(request):
    vendors = Vendor.get_all_vendors()
    vendorID = request.GET.get("vendor")
    if vendorID:
        products = Product.get_all_products_by_vendorid(vendorID)
        vendor = Vendor.objects.get(id=vendorID)
    else:
        products = Product.get_all_products()
        vendor = None

    vendor_product_map = {}
    vendor_product_map["products"] = products
    vendor_product_map["vendors"] = vendors
    vendor_product_map["vendor"] = vendor
    vendor_product_map["vendorID"] = vendorID

    return render(request, "vendor_products.html", vendor_product_map)

def store(request):
    cart = request.session.get("cart")
    if not cart:
        request.session["cart"] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get("category")
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data["products"] = products
    data["categories"] = categories

    return render(request, "category_products.html", data)
    

class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        # return redirect('')
        return redirect('Buyer:homepage')
    

    def get(self , request):
        print(f"{request.get_full_path()}")
        # return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')
        return HttpResponseRedirect(f'category_products'+f"{request.get_full_path().split('buyer/')[1]}")

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )
    

class Single_Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        # return redirect('')
        return redirect('Buyer:singlehomepage')


    def get(self , request):
        print(f"{request.get_full_path()}")
        # return HttpResponseRedirect(f'/buyer/single_products{request.get_full_path()[1:]}')
        return HttpResponseRedirect(f'single_products/{request.GET.get("product")}'+f"{request.get_full_path().split('buyer/')[1]}")
    
def single_store(request):
    cart = request.session.get("cart")
    if not cart:
        request.session["cart"] = {}

    productID = request.GET.get("product")
    products = Product.get_products_by_id(productID)

    product_map = {}
    product_map["products"] = products

    return render(request, "single_products.html", product_map)

def search(request):
    q=request.GET['q']
    data=Product.objects.filter(name__icontains=q)
    return render(request, 'search.html', {'data':data})

@login_required
def orderview(request ):
    customer = request.user
    orders = Order.get_orders_by_customer(customer)
    print(orders)
    return render(request , 'order.html'  , {'orders' : orders})
    
@login_required
def checkout(request):
    customer = request.user
    print(customer)
    cart = request.session.get('cart')
    products = Product.get_products_by_id(list(cart.keys()))
    print(customer, cart, products)

    for product in products:
        print(cart.get(str(product.id)))
        order = Order(customer=customer,
                        product=product,
                        price=product.price,
                        quantity=cart.get(str(product.id)))
        order.save()
    request.session['cart'] = {}

    return redirect('Buyer:order')

@login_required
def wishlist(request):
    products = Product.objects.filter(users_wishlist=request.user)
    return render(request, "user_wish_list.html", {"wishlist": products})

@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    product.users_wishlist.add(request.user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

@login_required
def remove_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])