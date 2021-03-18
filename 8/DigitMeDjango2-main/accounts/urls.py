from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),

    path('account/', views.accountSettings, name="account"),

    path('products/', views.products, name='products'),
    path('product_create/', views.product_create, name='product_create'),
    
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('update_customer/<str:pk>/', views.updateCustomer, name="update_customer"),

    path('orders/', views.Orders, name="orders"),
    path('order_create/', views.order_create, name='order_create'),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    
]