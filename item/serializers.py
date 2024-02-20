from rest_framework import serializers
from .models import Item, ItemImage


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ['image']


class ItemSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'sentimental_value',
                  'monetary_value', 'ownership_status', 'location',
                  'desired_disposition', 'category', 'user', 'images']
