from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AppointmentSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.doctor} - {self.date} - {self.time}"

class Appointment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    slot = models.OneToOneField(AppointmentSlot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.slot}"