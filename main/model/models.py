from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50)
    income = models.BigIntegerField()