from django.db import models


class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mean_radius = models.FloatField()
    mean_texture = models.FloatField()
    mean_perimeter = models.FloatField()
    mean_area = models.FloatField()
    mean_smoothness = models.FloatField()
    result = models.CharField(max_length=10)  # Change from 'result' to 'prediction_result'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.prediction_result} ({self.created_at})"