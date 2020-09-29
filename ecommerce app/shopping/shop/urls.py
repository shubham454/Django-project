from django.urls import path
from . import views
from rest_framework.authtoken import views as authview

urlpatterns = [
    path('register/', views.UserRegistration.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='user-login'),
    path('logout/', views.LogoutView.as_view(), name='user-logout'),
    path('get-api-token/', authview.obtain_auth_token, name='get-api-token'),
    path('product_list/', views.ProductList.as_view(), name='product_list'),
    path('product_list/<str:product_name>/', views.card_add, name='product-with-id'),
    path('product-select/', views.cart, name='product-select')
]
