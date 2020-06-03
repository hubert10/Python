from rest_framework import generics
from .models import Drink
from .serializers import DrinkSerializer


class ListDrinkView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer