from django.contrib import admin
from .models import Post
from .models import Company
from .models import Journey
from .models import Station


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('Name', 'WebUrl', 'WebUrlContactUs', 'CustomerServicePhone')
    search_fields = ('Name', 'WebUrl')


class StationAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Created', 'Updated')
    search_fields = ('Name',)

    ordering = ['Name', 'Created', 'Updated']


class JourneyAdmin(admin.ModelAdmin):
    list_display = ('DepartureStation', 'DelayAtDepartureStationMins', 'Created', 'Updated')
    search_fields = ('DepartureStation', 'ArrivalStation', 'DelayAtDepartureStationMins')
    date_hierarchy = 'Created'
    ordering = ['Company', 'ScheduledDepartureTime', 'Created', 'Updated']


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Company, CompanyAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Journey, JourneyAdmin)

admin.site.register(Post, PostAdmin)
