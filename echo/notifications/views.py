from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Alert, UserAlertPreference
from datetime import timedelta

# Create your views here.


@login_required
def snooze_alert(request, alert_id):
    alert = get_object_or_404(Alert, id=alert_id)
    pref, created = UserAlertPreference.objects.get_or_create(
        user=request.user,
        alert=alert
    )
    # Set snooze for 10 minutes (you can make this configurable)
    pref.snoozed_until = timezone.now() + timedelta(minutes=10)
    pref.save()

    return redirect('dashboard') 

@login_required
def mark_alert_as_read(request, alert_id):
    if request.method == 'POST':
        user_alert = get_object_or_404(UserAlertPreference, user=request.user, alert_id=alert_id)
        user_alert.is_read = True
        user_alert.save()
    return redirect('dashboard')


@login_required
def all_notifications(request):
    notifications = UserAlertPreference.objects.filter(user=request.user).order_by('-alert__start_time')
    return render(request, 'all_notifications.html', {'notifications': notifications})