from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="predictions")  # Link to logged-in user
    mean_radius = models.FloatField()
    mean_texture = models.FloatField()
    mean_perimeter = models.FloatField()
    mean_area = models.FloatField()
    mean_smoothness = models.FloatField()
    result = models.CharField(max_length=100)  # Store prediction result (Malignant/Benign)
    created_at = models.DateTimeField(default=now)  # Auto timestamp

    class Meta:
        ordering = ['-created_at']  # Order by latest predictions first

    def __str__(self):
        return f"Prediction by {self.user.username} on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"