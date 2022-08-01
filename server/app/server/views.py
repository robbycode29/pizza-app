from django.shortcuts import render


# api functionality

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from rest_framework import renderers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from server.models import Ingredient, Pizza, PizzaOrder
from server.serializers import IngredientSerializer, PizzaOrderSerializer, PizzaSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


# view sets

    # all entries

class PizzaOrderViewSet(viewsets.ModelViewSet):
    queryset = PizzaOrder.objects.all()
    serializer_class = PizzaOrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=True, methods=['GET'])
    def pizzas(self, request, pk=None):
        pizza_order = self.get_object()
        pizzas = pizza_order.pizzas.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def ingredients(self, request, pk=None):
        pizza_order = self.get_object()
        ingredients = pizza_order.ingredients.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def status(self, request, pk=None):
        pizza_order = self.get_object()
        return Response(pizza_order.status)

    @action(detail=True, methods=['POST'])
    def update_status(self, request, pk=None):
        pizza_order = self.get_object()
        pizza_order.status = request.data['status']
        pizza_order.save()
        return Response(pizza_order.status)


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=True, methods=['GET'])
    def ingredients(self, request, pk=None):
        pizza = self.get_object()
        ingredients = pizza.ingredients.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (permissions.IsAuthenticated,)


# user specific orders

class UserOrdersViewSet(viewsets.ModelViewSet):
    queryset = PizzaOrder.objects.all()
    serializer_class = PizzaOrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return PizzaOrder.objects.filter(user=self.request.user)

    @action(detail=True, methods=['GET'])
    def pizzas(self, request, pk=None):
        pizza_order = self.get_object()
        pizzas = pizza_order.pizzas.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def ingredients(self, request, pk=None):
        pizza_order = self.get_object()
        ingredients = pizza_order.ingredients.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def status(self, request, pk=None):
        pizza_order = self.get_object()
        return Response(pizza_order.status)

    @action(detail=True, methods=['POST'])
    def update_status(self, request, pk=None):
        pizza_order = self.get_object()
        pizza_order.status = request.data['status']
        pizza_order.save()
        return Response(pizza_order.status)

    
    
