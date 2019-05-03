from django.contrib import admin

from . import models


class ReviewInline(admin.TabularInline):
    model = models.Review


class HotelAdmin(admin.ModelAdmin):
    search_fields = (
        "name",
    )

    inlines = [
        ReviewInline,
    ]


admin.site.register(models.Hotel, HotelAdmin)


class RegRequestAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.RegRequest, RegRequestAdmin)


class HotelMessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.HotelMessage, HotelMessageAdmin)
