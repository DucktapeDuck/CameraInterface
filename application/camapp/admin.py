from django.contrib import admin

# Register your models here.
from camapp.models import Instance

# admin.site.register(Instances)

# Register the Admin classes for BookInstance using the decorator
@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ('type', 'time', 'accuracy', 'image_location')
    list_filter = ('type', 'time')

    fieldsets = (
        (None, {
            'fields': ('type', 'time')
        }),
        ('Object Detection Information', {
            'fields': ('accuracy', 'image_location')
        }),
    )