from django.db import models

class Hrac(models.Model):
    jmeno = models.CharField(max_length=100)
    klub = models.CharField(max_length=100)
    goly = models.IntegerField()

    def __str__(self):
        return f"{self.jmeno} ({self.klub})"