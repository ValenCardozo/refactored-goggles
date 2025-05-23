from django.contrib import admin

from products.models import Customer, Order, OrderDetail, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image')
    list_filter = ('name', 'price')
    search_fields = ('name', 'description')


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