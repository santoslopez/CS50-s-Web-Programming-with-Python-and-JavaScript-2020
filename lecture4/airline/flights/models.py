from django.db import models

# Create your models here.
class Airoport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    #origin = models.CharField(max_length=64)
    origin = models.ForeignKey(Airoport,on_delete=models.CASCADE)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    # return string representation of the object
    # cuando se invoca flights ya no devuelve un entero sino esto
    def __str__(self):
        return f"{self.id}: {self.origin}: to {self.destination}"
