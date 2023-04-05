from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50)
    income = models.BigIntegerField()
    testing = models.CharField(max_length=50, default='testing')

class CardSets(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50, null=True)
    series = models.CharField(max_length=50, null=True)
    printed_total = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    unlimited_legality = models.CharField(max_length=50, null=True)
    ptcgo_code = models.CharField(max_length=20, null=True)
    release_date = models.DateField(null=True)
    updated_at = models.DateTimeField(null=True)
    symbol_image_url = models.CharField(max_length=200, null=True)
    logo_image_url = models.CharField(max_length=200, null=True)

class TestTable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
