from django.contrib import admin

# Register your models here.
from django.contrib import admin
from rango.models import Page,Category
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page)