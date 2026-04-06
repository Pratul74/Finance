from django.contrib import admin
from .models import Record

# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'type', 'category', 'amount', 'note', 'created_at']
    list_filter=['type', 'category']
