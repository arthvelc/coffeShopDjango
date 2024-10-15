from django.contrib import admin

from orders.models import Order, OrderProduct

# Register your models here.
class OrderProductAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductAdmin]

admin.site.register(Order, OrderAdmin)
