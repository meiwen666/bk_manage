from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

class Address(models.Model):
    bk_ip = models.CharField(max_length=50)



class Cron(models.Model):
    minute = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(59)])
    hour = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(59)])
    day = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(31)])
    month = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(12)])
    week = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(7)])
    ip =models.CharField(max_length=20)
    s_path= models.CharField(max_length=200)
    d_path= models.CharField(max_length=200)
    log_path = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    bkip = models.ForeignKey(to='Address',on_delete=models.CASCADE)


