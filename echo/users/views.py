from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from notifications.models import Alert, UserAlertPreference
from django.db.models import Q


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

from django.db.models import Q

@login_required
def dashboard(request):
    user = request.user
    now = timezone.now()

    # Active alerts for this user
    active_alerts = Alert.objects.filter(
        is_active=True,
        start_time__lte=now,
        expiry_time__gte=now
    ).filter(
        Q(entire_organization=True) |
        Q(users=user) |
        Q(teams=user.team)
    ).distinct()

    # Alerts snoozed by user
    snoozed_alerts = UserAlertPreference.objects.filter(
        user=user,
        snoozed_until__gt=now
    ).values_list('alert_id', flat=True)

    # Alerts read by user
    read_alerts = UserAlertPreference.objects.filter(
        user=user,
        is_read=True
    ).values_list('alert_id', flat=True)

    # Final alerts: active alerts minus snoozed and read
    alerts_to_show = active_alerts.exclude(id__in=list(snoozed_alerts) + list(read_alerts))

    return render(request, 'dashboard.html', {'alerts': alerts_to_show})



 
        
