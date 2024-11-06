from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='Base'),
    path('Brands/', views.base, name='brands'),

    # Correcting the 'buy_now' URL to point to the proper view
    path('order/', views.order, name='order'),

    path('submitpayment/', views.submit_payment, name='submitpayment'),
    path('register/', views.Register, name='Register'),
    path('cart/', views.cart, name='cart'),  # Cart page
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('profile/', views.profile, name='profile'),

    path('smart_equipments/', views.smart_equipments, name='smart_equipments'),
    path('products/', views.products, name='products'),

    path('seeds/', views.seeds, name='seeds'),
    path('login_first/', views.login_first, name='login_first'),
    path('about/', views.about, name='about'),
    path('equipments/', views.equipments, name='equipments'),
]
