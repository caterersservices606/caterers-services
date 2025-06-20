from django.db import models

class EventBooking(models.Model):
    # Status choices
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirm", "Confirm"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
        ("done", "Done"),
    ]

    name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=20)
    description = models.TextField()
    rule = models.BooleanField()
    time_slots = models.JSONField(default=list)  # contains list of time slot dictionaries
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    
