from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    readonly_fields = ['created_at']
    raw_id_fields = ("liked_by",)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat", "сomplainter")

admin.site.register(Complaint, ComplaintAdmin)

admin.site.register(Flat, FlatAdmin)