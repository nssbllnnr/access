from django.contrib import admin

# Register your models here.
from .models import Employees
from .models import Members

admin.site.register(Employees)
admin.site.register(Members)
