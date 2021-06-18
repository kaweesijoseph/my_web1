from django.contrib import admin

from .models import *

# Register your models here.
admin.site.site_header = 'Kaweesi Joseph  Administration'


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'Email_address', 'date_time',)


admin.site.register(Feedback, FeedbackAdmin)
