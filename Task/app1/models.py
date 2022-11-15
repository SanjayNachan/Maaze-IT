from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    salary=models.FloatField()
    task=models.CharField(max_length=50)
    image=models.FileField(upload_to='app1/files/covers', blank=True, default=None)