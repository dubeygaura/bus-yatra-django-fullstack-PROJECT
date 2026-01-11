from django.contrib import admin

from myapp.models import admintbl, routestbl, managebustbl

# Register your models here.
admin.site.register(admintbl)
admin.site.register(routestbl)
admin.site.register(managebustbl)