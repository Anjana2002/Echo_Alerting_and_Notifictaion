from django.contrib import admin
from .models import Alert, User, Team, NotificationDelivery, UserAlertPreference
# Register your models here.

admin.site.register(Team)
admin.site.register(Alert)
admin.site.register(User)
admin.site.register(UserAlertPreference)
admin.site.register(NotificationDelivery)