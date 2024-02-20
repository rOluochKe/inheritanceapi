from django.urls import path
from .views import CategoryCreate, CategoryDetail

urlpatterns = [
    path('', CategoryCreate.as_view(), name='category-create'),
    path('<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
]
