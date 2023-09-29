from django.urls import path
from .views import ProductListCreateView, StockListCreateView, StockInListCreateView, StockOutListCreateView, PaymentConfirmationListCreateView
from .views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('stocks/', StockListCreateView.as_view(), name='stock-list-create'),
    path('stockin/', StockInListCreateView.as_view(), name='stockin-list-create'),
    path('stockout/', StockOutListCreateView.as_view(), name='stockout-list-create'),
    path('payment/', PaymentConfirmationListCreateView.as_view(), name='paymentconfirmation-list-create'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    # Add more URLs for other views here
]
