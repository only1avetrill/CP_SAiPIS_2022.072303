from django.contrib import admin
from .models import *


class ExecutorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Executor._meta.get_fields()]


class AdsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ad._meta.get_fields()]


admin.site.register(Executor, ExecutorAdmin)
admin.site.register(Ad, AdsAdmin)
