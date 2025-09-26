from django.db import models
from django.conf import settings
# Create your models here.
class Alert(models.Model):
    SEVERITY_CHOICES = [
        ('info', 'Info'),
        ('warning', 'Warning'),
        ('critical', 'Critical')
    ]
    title = models.CharField(max_length=200)
    message = models.TextField()
    severity = models.CharField(max_length=50, choices=SEVERITY_CHOICES)
    start_time = models.DateTimeField()
    expiry_time = models.DateTimeField()
    remainder_freq = models.IntegerField(default=120)
    
    teams = models.ManyToManyField('users.Team', blank=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    entire_organization = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.title} ({self.severity})"
    
class NotificationDelivery(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    delivered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('delivered', 'Delivered'),
            ('read', 'Read'),
            ('snoozed', 'Snoozed'),
        ],
        default='delivered'
    )

    def __str__(self):
        return f"{self.alert.title} → {self.user.username} ({self.status})"
    
class UserAlertPreference(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    snoozed_until = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.alert.title}"
    
class UserSettings(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    snooze_minutes = models.PositiveIntegerField(default=10)  # default 10 minutes

    def __str__(self):
        return f"{self.user.username} Settings"