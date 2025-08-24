
from django.db import models

# Create your models here.
class emp(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_age = models.IntegerField()
    mp_email = models.EmailField()
    emp_salary = models.IntegerField()