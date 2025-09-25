from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Alert, UserAlertPreference
from datetime import timedelta

# Create your views here.
@login_required
def snooze_alert(request, alert_id):
    alert = get_object_or_404(Alert, id=alert_id)
    user = request.user

    # snooze for 2 hours (can customize)
    snooze_until = timezone.now() + timedelta(hours=2)

    # create or update preference
    pref, created = UserAlertPreference.objects.get_or_create(
        alert=alert,
        user=user,
    )
    pref.snoozed_until = snooze_until
    pref.save()

    return redirect('dashboard')