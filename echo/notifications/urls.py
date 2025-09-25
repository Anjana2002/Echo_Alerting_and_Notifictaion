from django.urls import path
from . import views

urlpatterns = [
    path('snooze/<int:alert_id>/', views.snooze_alert, name='snooze_alert'),
]