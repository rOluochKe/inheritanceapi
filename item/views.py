from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from .models import ItemImage


class ItemList(APIView):
    """
    API endpoint that allows items to be listed and created.
    """
    def get(self, request):
        """
        Retrieve a list of all items.
        """
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new item.
        """
        item_serializer = ItemSerializer(data=request.data)
        if item_serializer.is_valid():
            # Save the item
            item_instance = item_serializer.save()

            # Handle item images
            # Assuming images are sent as list
            images_data = request.data.getlist('images')
            item_images = []
            for image in images_data:
                item_images.append(ItemImage(item=item_instance, image=image))
            ItemImage.objects.bulk_create(item_images)

            return Response({
                "message": "Item and images created successfully",
                "data": item_serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(item_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class ItemDetail(APIView):
    """
    API endpoint that allows specific items to be retrieved, updated, or
    deleted.
    """
    def get_object(self, pk):
        """
        Helper method to retrieve a specific category object.
        """
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve a item by ID.
        """
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a item by ID.
        """
        item = self.get_object(pk)
        item_serializer = ItemSerializer(item, data=request.data)
        if item_serializer.is_valid():
            # Save updated item details
            item_instance = item_serializer.save()

            # Handle image updates
            images_data = request.data.getlist('images')
            item_images = []
            for image in images_data:
                item_images.append(ItemImage(item=item_instance, image=image))
            ItemImage.objects.filter(item=item_instance).delete()
            ItemImage.objects.bulk_create(item_images)

            return Response({
                "message": "Item and images updated successfully",
                "data": item_serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response(item_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a category by ID.
        """
        item = self.get_object(pk)
        item.delete()
        return Response({"message": "Item deleted successfully"},
                        status=status.HTTP_204_NO_CONTENT)
