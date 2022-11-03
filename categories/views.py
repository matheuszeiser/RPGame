from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer


class CreateCategoryView(generics.CreateAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects
