from django.contrib import admin
from .models import (
    DjangoJob, DjangoJobExecution
)
# Register your models here.
@admin.register(DjangoJob)
class DjangoJobAdmin(admin.ModelAdmin):
    pass
@admin.register(DjangoJobExecution)
class DjangoJobExecutionAdmin(admin.ModelAdmin):
    pass