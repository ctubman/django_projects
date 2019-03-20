from django.contrib import admin

# Register your models here.

from unesco.models import Site, Category, ISO, Region, State

admin.site.register(Site)
admin.site.register(Category)
admin.site.register(ISO)
admin.site.register(Region)
admin.site.register(State)