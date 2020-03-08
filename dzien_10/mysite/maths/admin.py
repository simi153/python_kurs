from django.contrib import admin
from maths.models import Math


# Register your models here.

class MathAdmin(admin.ModelAdmin):
    list_display = ["id", "operation", "a", "b", "created"]
    readonly_fields = ['created']
    list_filter = ['operation']
    search_fields = ['a', 'b']


admin.site.register(Math, MathAdmin)
