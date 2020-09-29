from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import (LoginSerializer, UserSerializer,
                         ProductSerializer)
from .models import User, Product, OrderItem
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from django.contrib.auth import login, logout


class LoginView(APIView):
    permission_classes = [AllowAny, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(UserRegistration(user.data))


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response()


class UserRegistration(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated]


@api_view()
def card_add(request, product_name):
    """
    This view function is used to add product in session.
    for that we can end url as "http://127.0.0.1:8000/product_list/<product_name>/"
    """
    product = Product.objects.get(product_name=product_name)
    request.session[product.product_name] = product.product_name
    return Response({'msg': 'your object is added'})


@api_view()
def cart(request):
    """
    This view function is used to list out the products in session with product list and there prices.
    for that we can end url as "http://127.0.0.1:8000/product-select/"
    """
    products = Product.objects.all()
    product_name_list = []
    price_list = []
    for product in products:
        if product.product_name in request.session:
            product_name = request.session.get(product.product_name)
            price = product.price
            product_name_list.append(product_name)
            price_list.append(product.price)
            order = OrderItem.objects.create(product=Product.objects.get(product_name=product_name),
                                             quantity=1,
                                             price=price,
                                             order=True)
        else:
            continue
    p_dict = {'products selected': product_name_list,
              'price': price_list,
              'total price': sum(price_list)}
    return Response(p_dict)
