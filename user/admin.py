from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'location',
                    'phone_number', 'date_of_birth', 'profile_picture')
    search_fields = ('username', 'email', 'first_name', 'last_name',
                     'phone_number')
