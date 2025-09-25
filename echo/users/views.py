from django.shortcuts import render, redirect
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

@login_required
def dashboard(request):
    user = request.user
    now = timezone.now()

    active_alerts = Alert.objects.filter(
        is_active=True,
        start_time__lte=now,
        expiry_time__gte=now
    ).filter(
        Q(entire_organization=True) |
        Q(users=user) |
        Q(teams=user.team)
    ).distinct()

    snoozed_alerts = UserAlertPreference.objects.filter(
        user=user,
        snoozed_until__gt=now
    ).values_list('alert_id', flat=True)

    print("Snoozed alert IDs:", list(snoozed_alerts))   # 👈 check which IDs are snoozed
    print("Active before exclude:", list(active_alerts.values_list("id", flat=True)))

    active_alerts = active_alerts.exclude(id__in=snoozed_alerts)

    print("Active after exclude:", list(active_alerts.values_list("id", flat=True)))

    return render(request, 'dashboard.html', {'alerts': active_alerts})


    
        
