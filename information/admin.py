from django.contrib import admin
from information.models import Train, Station, Website


class TrainAdmin(admin.ModelAdmin):
    list_display = ('trainno', 'trainname', 'source', 'destination', 'depart', 'arrival', 'kms', 'ec', 'cc')


admin.site.register(Train, TrainAdmin)


class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'station')


admin.site.register(Station, StationAdmin)


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Website, WebsiteAdmin)


# Register your models here.
# Aarsh Saxena (21bec001)
