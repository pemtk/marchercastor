from rest_framework import serializers

from api.models import Category, Products


class CategorySerializer(serializers.ModelSerializer): # forms.ModelForm
    class Meta:
        model = Category
        fields = [
            'nom_cat',
            'images',
            'timestamp',
            'content',
            'timestamp',
        ]
    

class ProductSerializer(serializers.ModelSerializer): # forms.ModelForm
    class Meta:
        model = ProductSerializer
        fields = [
            'name',
            'price',
            'images',
            'categories',
            'timestamp',
        ]