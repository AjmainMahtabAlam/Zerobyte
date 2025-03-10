from django.db import models

class Package(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_transit", "In Transit"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]

    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)  # Soft delete field

    def delete(self, *args, **kwargs):
        """Override delete method to implement soft delete."""
        self.is_deleted = True
        self.save()

    def restore(self):
        """Method to restore a soft-deleted package."""
        self.is_deleted = False
        self.save()

    def __str__(self):
        return f"Package from {self.sender} to {self.recipient}"
