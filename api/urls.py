from django.urls import path
from .views import BuyerAPIView, ProductAPIView, ProductDetailAPIView

urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('', ProductAPIView.as_view()),
    path('buyers/', BuyerAPIView.as_view()),
]