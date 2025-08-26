from django.contrib import admin

from biodata2.models import Feedback, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Feedback)