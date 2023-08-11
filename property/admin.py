from django.contrib import admin
from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    list_display = ('address',
                    'price',
                    'new_building',
                    'construction_year',
                    'town',
                    )
    list_editable = ['new_building']
    readonly_fields = ['created_at']
    raw_id_fields = ("liked_by",)


class FlatInline(admin.TabularInline):
    model = Flat.owned_by.through
    raw_id_fields = ("flat",)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat", "сomplainter")


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats", )
    search_fields = ('name',)
    inlines = [
        FlatInline,
    ]
