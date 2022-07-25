from dataclasses import fields
from rest_framework import serializers
from .models import Shop, ShopPictures

class ShopsPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopPictures
        fields = ["picture"]


class ShopsSerializer(serializers.HyperlinkedModelSerializer):
    pictures = serializers.SerializerMethodField()
    class Meta:
        model = Shop
        fields = ["id","title","description","pictures"]
    
    def get_pictures(self,obj):
        selected_pictures = ShopPictures.objects.filter(
            shop=obj).distinct()
        return ShopsPicturesSerializer(selected_pictures, many=True).data