from django.db import models
from users.models import User
from hostels_app.models import Hostel

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name="reviews")
    rating = models.FloatField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("user", "hostel")

    def __str__(self):
        return f"Review by {self.user.email} for {self.hostel.name}"
