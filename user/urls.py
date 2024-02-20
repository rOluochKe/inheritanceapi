from django.urls import path
from .views import RegisterUser, ObtainToken, UserDetails, UpdateUser, Logout

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', ObtainToken.as_view(), name='login'),
    path('user-details/', UserDetails.as_view(), name='user-details'),
    path('user-update/', UpdateUser.as_view(), name='user-update'),
    path('logout/', Logout.as_view(), name='logout'),
]
