from django.db import models

# Create your models here.
class Patient(models.Model):
    p_name = models.CharField(max_length=15)
    p_group_blood = models.CharField(max_length=5)
    p_unit = models.IntegerField()
    p_age = models.IntegerField()
    p_phone_no=models.BigIntegerField()
    p_email = models.EmailField()
    p_date = models.DateTimeField()

class Donor(models.Model):
    d_name1 = models.CharField(max_length=15)
    d_group_blood1 = models.CharField(max_length=5)
    d_unit1 = models.IntegerField()
    d_age1 = models.IntegerField()
    d_phone_no1 = models.BigIntegerField()
    d_email1 = models.EmailField()
    d_date1 = models.DateTimeField()
