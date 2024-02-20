from django.contrib import admin
from .models import Item, ItemImage


class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline]
    list_display = ('name', 'description', 'category', 'user',
                    'sentimental_value', 'monetary_value', 'ownership_status',
                    'location', 'desired_disposition')
    search_fields = ('name', 'description', 'category__name', 'user__username')
