from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from skills.models import Skill
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdminOrReadOnly


class CreateCategoryView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = CategorySerializer
    queryset = Category.objects


class UpdateDeleteCategoryView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects
    pk = 'pk'


class ListCategoriesView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
