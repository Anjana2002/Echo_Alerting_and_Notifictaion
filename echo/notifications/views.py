from django.shortcuts import get_object_or_404, redirect
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

