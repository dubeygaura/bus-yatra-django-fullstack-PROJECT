from django.db import models

# Create your models here.
class admintbl(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id},{self.username},{self.password}"

class routestbl(models.Model):
    id = models.AutoField(primary_key=True)
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    distance=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id},{self.source},{self.destination},{self.distance},{self.duration}"

class managebustbl(models.Model):
    id = models.AutoField(primary_key=True)
    busname=models.CharField(max_length=100)
    routeid=models.CharField(max_length=100)
    dtime=models.CharField(max_length=100)
    totalseet=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id},{self.busname}"









