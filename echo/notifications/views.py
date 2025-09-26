from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Alert, UserAlertPreference, UserSettings
from datetime import timedelta

# Create your views here.


@login_required
def snooze_alert(request, alert_id):
    alert = get_object_or_404(Alert, id=alert_id)
    pref, created = UserAlertPreference.objects.get_or_create(
        user=request.user,
        alert=alert
    )
  
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

@login_required
def settings_view(request):
    try:
        user_settings = UserSettings.objects.get(user=request.user)
    except UserSettings.DoesNotExist:
        user_settings = UserSettings.objects.create(user=request.user)

    if request.method == "POST":
        snooze_minutes = request.POST.get("snooze_minutes")
        if snooze_minutes and snooze_minutes.isdigit():
            user_settings.snooze_minutes = int(snooze_minutes)
            user_settings.save()
        return redirect("settings")

    return render(request, "settings.html", {"settings": user_settings})