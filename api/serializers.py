from rest_framework import serializers

from .models import Category, Products


class CategorySerializer(serializers.ModelSerializer): # forms.ModelForm
    class Meta:
        model = Category
        fields = [
            'nom_cat',
            'images',
            'timestamp',
        ]
    

class ProductSerializer(serializers.ModelSerializer): # forms.ModelForm
    class Meta:
        model = Products
        fields = [
            'name',
            'price',
            'images',
            'categories',
            'timestamp',
        ]