from rest_framework import generics
from .models import Attribute
from .serializers import AttributeSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import IsCharacterOwner
from django.shortcuts import get_object_or_404
from characters.models import Character


class UpdateAttributes(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCharacterOwner]

    serializer_class = AttributeSerializer
    queryset = Attribute

    def get_object(self):
        character = get_object_or_404(Character, id=self.kwargs["pk"])
        self.check_object_permissions(self.request, character)
        attributes = get_object_or_404(Attribute, id=character.attributes.id.urn[9:])
        return attributes
