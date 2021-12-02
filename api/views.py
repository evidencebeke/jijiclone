
from rest_framework import generics, permissions, viewsets
from .models import Product, Buyer
from .serializers import BuyerSerializer, ProductSerializer
from .permissions import IsAuthorOrReadOnly

class ProductAPIView(generics.ListCreateAPIView):
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    
    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BuyerAPIView(generics.ListAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


