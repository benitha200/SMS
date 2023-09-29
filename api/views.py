from rest_framework import generics
from .models import Product, Stock, StockOut, StockIn, Payment_confirmation
from .serializers import ProductSerializer, StockSerializer, StockInSerializer, StockOutSerializer, \
    PaymentConfirmationSerializer,UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class UserRegistrationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return Response({'success':'true','message': 'Login successful','username':user.get_username()}, status=status.HTTP_200_OK)
            else:
                return Response({'success':'false','message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StockListCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockInListCreateView(generics.ListCreateAPIView):
    queryset = StockIn.objects.all()
    serializer_class = StockInSerializer


class StockOutListCreateView(generics.ListCreateAPIView):
    queryset = StockOut.objects.all()
    serializer_class = StockOutSerializer


class PaymentConfirmationListCreateView(generics.ListCreateAPIView):
    queryset = Payment_confirmation.objects.all()
    serializer_class = PaymentConfirmationSerializer
