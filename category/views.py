from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Category
from .serializers import CategorySerializer


class CategoryCreate(APIView):
    """
    API endpoint that allows categories to be created.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get a list of all categories.
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new category.
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    """
    API endpoint that allows specific categories to be retrieved, updated, or
    deleted.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """
        Helper method to retrieve a specific category object.
        """
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404("Category does not exist")

    def get(self, request, pk):
        """
        Retrieve a category by ID.
        """
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a category by ID.
        """
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a category by ID.
        """
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
