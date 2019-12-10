from django.shortcuts import render
from rest_framework import generics, mixins
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Products


# Create your views here.

class CategoryView(generics.RetrieveUpdateDestroyAPIView): # DetailView CreateView FormView
    lookup_field            = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = CategorySerializer


    def get_queryset(self):
        return Category.objects.all()

    
class ProductsView(generics.RetrieveUpdateDestroyAPIView): # DetailView CreateView FormView
    lookup_field            = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = ProductSerializer


    def get_queryset(self):
        return Products.objects.all()

    