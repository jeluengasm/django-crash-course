from django.contrib import admin

# Register your models here.

from .models import * # We must import this table created and migrated from "models.py"

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)