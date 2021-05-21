from django.contrib import admin

from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', "order_status")


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
