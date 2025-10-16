from django.contrib import admin
from orders.models import order
class orderAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'order_status', 'total')

    search_fields = ('owner__user__username', 'order_status')
    list_filter = ('order_status',)



admin.site.register(order, orderAdmin)

# Register your models here.
