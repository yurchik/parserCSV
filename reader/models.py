from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')


class Regions(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Countries(models.Model):
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parameter = models.IntegerField(default=0)