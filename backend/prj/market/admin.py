from django.contrib import admin
from market.models import UserProfile, Category, SubCategory, Product, Order, OrderProduct, Store

from market.models import Notification

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['get_small_image', 'name', 'username']

admin.site.register(UserProfile, UserProfileAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag']

admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']

admin.site.register(SubCategory, SubCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'get_small_image']
    list_filter = ['category']

admin.site.register(Product, ProductAdmin)


class OrderProductAdmin(admin.TabularInline):
    model = OrderProduct
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductAdmin,]
    list_display = ['consumer', 'created_at']


admin.site.register(Order, OrderAdmin)



class StoreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Store, StoreAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['product', 'provider', 'consumer']

admin.site.register(Notification, NotificationAdmin)



