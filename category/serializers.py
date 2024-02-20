from rest_framework import serializers
from .models import Category
from item.serializers import ItemSerializer
from item.models import Item


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'items']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        items = Item.objects.filter(category=instance)
        item_serializer = ItemSerializer(items, many=True)
        representation['items'] = item_serializer.data
        return representation
