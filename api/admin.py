from django.contrib import admin

# Register your models here.
from import_export import resources
from api.models import Item, ItemImage, UserProfile, Category
from import_export.admin import ImportExportModelAdmin


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class ItemResource(resources.ModelResource):
    class Meta:
        model = Item


class CategoryAdmin(ImportExportModelAdmin):
    resources_class = CategoryResource


class ItemAdmin(ImportExportModelAdmin):
    resource_class = ItemResource


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage)
admin.site.register(UserProfile)
