from django.urls import path
from . import views

urlpatterns = [
    path('snooze/<int:alert_id>/', views.snooze_alert, name='snooze_alert'),
    path('alerts/mark-read/<int:alert_id>/', views.mark_alert_as_read, name='mark_alert_as_read'),
    path('notifications/', views.all_notifications, name='all_notifications'),
    path('settings/', views.settings_view, name='settings'),

]