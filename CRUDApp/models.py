from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    empID = models.CharField(max_length=70)
    empName = models.CharField(max_length=60)
    empDesg = models.CharField(max_length=70)
    empSlaray = models.IntegerField()

