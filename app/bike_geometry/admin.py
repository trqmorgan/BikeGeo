from django.contrib import admin

from .models import BikeBrand, BikeModel, BikeGeometry


class BikeModelInline(admin.TabularInline):
    model = BikeModel
    extra = 3


class BikeBrandAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["brand_name"]}),
        ("Date information", {"fields": ["date_added"]}),
    ]
    list_display = ["brand_name", "date_added", "was_added_recently"]
    search_fields = ["brand_name"]
    inlines = [BikeModelInline]


class BikeGeometryInline(admin.TabularInline):
    model = BikeGeometry
    extra = 1


class BikeModelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["brand_name"]}),
        ("Bike information", {"fields": ["model_name", "model_year"]}),
    ]
    list_display = ["brand_name", "model_name", "model_year"]
    search_fields = ["brand_name__brand_name", "model_name", "model_year"]
    inlines = [BikeGeometryInline]


admin.site.register(BikeBrand, BikeBrandAdmin)
admin.site.register(BikeModel, BikeModelAdmin)