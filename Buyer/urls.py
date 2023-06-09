from django.urls import path
from . import views
from .views import Index ,store,single_store, Cart, orderview, checkout

app_name = 'Buyer'

urlpatterns = [

    path('vendor_products/', views.vendor_item, name='vendor_products'),
    path('', Index.as_view(), name='homepage'),
    path('search', views.search, name='search'),
    path('category_products/', store , name='store'),
    path('single_products/', single_store , name='singlestore'),
    path('cart', Cart.as_view() , name='cart'),
    path('order', orderview, name='order'),
    path('check-out', checkout , name='check-out'),
    path("wishlist", views.wishlist, name="wishlist"),
    path("wishlist/add_to_wishlist/<int:id>", views.add_to_wishlist, name="user_add_wishlist"),
    path("wishlist/remove_to_wishlist/<int:id>", views.remove_to_wishlist, name="user_remove_wishlist"),

]
