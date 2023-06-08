from django.db import models

# Create your models here.
class Data(models.Model):
    slno=models.IntegerField()
    name=models.CharField(max_length=250)
    description=models.CharField(max_length=250)
    def __str__(self):
        return self.name