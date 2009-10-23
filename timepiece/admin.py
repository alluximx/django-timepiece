from django.contrib import admin
from timepiece import models as timepiece

class ActivityAdmin(admin.ModelAdmin):
    model = timepiece.Activity
    list_display = ('code', 'name')

class EntryAdmin(admin.ModelAdmin):
    model = timepiece.Entry
    list_display = ('user',
                    'project',
                    'activity',
                    'start_time',
                    'end_time',
                    'hours',
                    'is_closed',
                    'is_paused')
    list_filter = ['project']
    search_fields = ['user', 'project', 'activity', 'comments']
    date_hierarchy = 'start_time'

class ProjectAdmin(admin.ModelAdmin):
    model = timepiece.Project
    # list_display = ('name', 'is_active', 'log_count', 'total_hours')


class RepeatPeriodAdmin(admin.ModelAdmin):
    list_display = ('project', 'count', 'interval')
    list_filter = ('interval',)
admin.site.register(timepiece.RepeatPeriod, RepeatPeriodAdmin)


class BillingWindowAdmin(admin.ModelAdmin):
    list_display = ('id', 'period', 'date', 'end_date')
    list_filter = ('period',)
admin.site.register(timepiece.BillingWindow, BillingWindowAdmin)


admin.site.register(timepiece.Activity, ActivityAdmin)
admin.site.register(timepiece.Entry, EntryAdmin)
admin.site.register(timepiece.Project, ProjectAdmin)
