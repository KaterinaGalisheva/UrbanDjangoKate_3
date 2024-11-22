from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Buyer, Horse

# Register your models here.

# Админка для модели Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    # Поля для отображения в списке
    list_display = ('name', 'age', 'purchased_horses')
    # Поля для поиска
    search_fields = ('id', 'name')
    # Фильтры
    list_filter = ('age',)
    # Сортировка
    ordering = ('id',)
    # Форма для редактирования
    fieldsets = (
        (None, {
            'fields': ('name', 'age')
        }),
    )



# Админка для модели Horse
@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):
    # Поля для отображения в списке
    list_display = ('name', 'sex', 'breed', 'age', 'height', 'location', 'cost', 'photo_display', 'buyer_count')
    
    # Поля для поиска
    search_fields = ('name', 'sex', 'breed', 'location', 'cost')
    
    # Фильтры
    list_filter = ('breed', 'sex', 'age', 'location')
    
    # Сортировка
    ordering = ('name',)
    
    # Форма для редактирования
    fieldsets = (
        (None, {
            'fields': ('name', 'sex', 'breed', 'age', 'height', 'location', 'description', 'cost', 'photo', 'buyer')
        }),
    )

    # Отображение количества покупателей в списке лошадей
    def buyer_count(self, obj):
        return obj.buyer.count()
    buyer_count.short_description = 'Количество покупателей'

    # Отображение изображения в списке
    def photo_display(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" style="width: 50px; height: auto;" />')
        return "Нет изображения"
    photo_display.short_description = 'Фото'
