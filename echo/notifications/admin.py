from django.contrib import admin
from .models import Alert, NotificationDelivery, UserAlertPreference


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('title', 'severity', 'start_time', 'expiry_time', 'is_active')
    list_filter = ('severity', 'is_active', 'start_time', 'expiry_time', 'entire_organization')
    filter_horizontal = ('teams', 'users')



admin.site.register(UserAlertPreference)
admin.site.register(NotificationDelivery)
