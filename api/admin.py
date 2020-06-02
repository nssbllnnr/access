from django.contrib import admin
from .models import *

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass

@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    pass

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    pass
