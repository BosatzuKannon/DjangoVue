from django.contrib import admin
from .models import Category, Type, Element

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')    
    search_fields = ('id', 'title')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')    
    search_fields = ('id', 'title')

class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')    
    search_fields = ('id', 'title', 'description')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Element, ElementAdmin)
