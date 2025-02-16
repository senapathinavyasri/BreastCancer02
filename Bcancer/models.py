from django.db import models

# Create your models here.
# class DoctorProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     specialization = models.CharField(max_length=100)
#     experience = models.IntegerField()


# class Appointment(models.Model):
#     patient = models.ForeignKey(User, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor")
#     date = models.DateField()
#     time = models.TimeField()
#     status = models.CharField(max_length=20, default="Pending")
