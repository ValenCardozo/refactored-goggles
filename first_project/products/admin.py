from decimal import Decimal as D
from django.contrib import admin

from products.models import (
    Category,
    Customer,
    Order,
    Product,
    OrderDetail,
)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image', 'category')
    list_filter = ('name', 'category')
    search_fields = ('name', 'description')
    actions = ['update_price_15']

    def update_price_15(self, request, queryset):
        for product in queryset:
            product.price = product.price * D(1.15)
            product.save()
        self.message_user(
            request,
            "Se proceso correctamente aumento de precios",
            level='success'
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_filter = ('name', 'email', 'phone')
    search_fields = ('name', 'email')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date')


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')
    list_filter = ('order', 'quantity')
    search_fields = ('order', 'product')