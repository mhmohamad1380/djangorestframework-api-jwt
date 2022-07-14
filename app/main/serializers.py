from dataclasses import fields
from rest_framework import serializers
from .models import Food, FoodsPictures

class FoodsPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodsPictures
        fields = ["picture"]


class FoodsSerializer(serializers.HyperlinkedModelSerializer):
    pictures = serializers.SerializerMethodField()
    class Meta:
        model = Food
        fields = ["id","title","description","pictures"]
    
    def get_pictures(self,obj):
        selected_pictures = FoodsPictures.objects.filter(
            food=obj).distinct()
        return FoodsPicturesSerializer(selected_pictures, many=True).data