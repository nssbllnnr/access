from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Employees)
admin.site.register(Device)
admin.site.register(Access)
admin.site.register(History)

