from math import remainder
from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
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
    
    teams = models.ManyToManyField('Team', blank=True)
    users = models.ManyToManyField('User', blank=True)
    entire_organization = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True) 
    def __str__(self):
        return f"{self.title} ({self.severity})"
    
class NotificationDelivery(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
        return f"{self.alert.title} → {self.user.name} ({self.status})"
    
class UserAlertPreference(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    snoozed_until = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.name} - {self.alert.title}"
    
    