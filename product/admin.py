from django.utils import timezone
from django.contrib import admin

from product.models import Category, Product


# register models in django-admin panel

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at', 'modified_at', 'added_24_hours_ago')
    search_fields = ['name']

    # return boolean if product was added 24 hours ago
    def added_24_hours_ago(self, obj):
        datetime_now = timezone.now()
        datetime_before_24_hours = datetime_now - timezone.timedelta(hours=24)
        return datetime_before_24_hours <= obj.created_at <= datetime_now

    added_24_hours_ago.boolean = True


admin.site.register(Product, ProductAdmin)

admin.site.register(Category)
