from django.contrib.auth.models import User
from rest_auth.views import LogoutView
from rest_framework import generics, permissions
from myproject.main import serializers
from myproject.main.models import Product


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.UserRegisterSerializer


class CustomLogoutView(LogoutView):
    permissions_classes = (permissions.IsAuthenticated, )


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = serializers.ProductSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
