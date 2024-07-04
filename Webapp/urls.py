from django.urls import path
from Webapp import views

urlpatterns=[
    path('',views.home_page,name="home"),
    path('contact/', views.contact, name="contact"),
    path('category/', views.category, name="category"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('products/', views.products, name="products"),
    path('products_filtered/<cat_name>/', views.products_filtered, name="products_filtered"),
    path('single_product/<int:Pro_id>/', views.single_product, name="single_product"),
    path('LR/', views.LR, name="LR"),
    path('save_registration/', views.save_registration, name="save_registration"),
    path('User_login/', views.User_login, name="User_login"),
    path('User_Logout/', views.User_Logout, name="User_Logout"),
    path('save_cart/', views.save_cart, name="save_cart"),
    path('cart/', views.cart, name="cart"),

]