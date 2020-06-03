from django.urls import path
from .views import ListDrinkView


urlpatterns = [
    path('restaurent/', ListDrinkView.as_view(), name="drinks-all")
]