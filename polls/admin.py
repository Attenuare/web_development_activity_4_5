from django.contrib import admin
from .models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
	list_display = ('description', 'date')


admin.site.register(Schedule, ScheduleAdmin)