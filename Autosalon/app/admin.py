from django.contrib import admin
from .models import Brand, BrandCategory, Color, ColorCategory, Car, CarCategory

# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'updated', 'category', 'published')
    list_display_links = ('title',)
    list_editable = ('published', 'category')
    list_filter = ('published',)
    search_fields = ('title', 'content')


admin.site.register(Brand, BrandAdmin)
admin.site.register(BrandCategory)


# -----------------------------------------------------------------------------------------


class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'updated', 'category', 'published')
    list_display_links = ('title',)
    list_editable = ('published', 'category')
    list_filter = ('published',)
    search_fields = ('title', 'content')


admin.site.register(Color, ColorAdmin)
admin.site.register(ColorCategory)


# -----------------------------------------------------------------------------------------


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'updated', 'category', 'published')
    list_display_links = ('title',)
    list_editable = ('published', 'category')
    list_filter = ('published',)
    search_fields = ('title', 'content')


admin.site.register(Car, CarAdmin)
admin.site.register(CarCategory)

