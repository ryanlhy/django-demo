from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50)
    income = models.BigIntegerField()