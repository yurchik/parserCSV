from django.db import models


class Regions(models.Model):
    name = models.CharField(max_length=100)


class Countries(models.Model):
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parameter = models.IntegerField