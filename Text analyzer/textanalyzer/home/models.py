from msilib.schema import Class
from django.db import models
import string
from matplotlib.pyplot import text
import datetime
# Create your models here.

class Mytext(models.Model):
    djtext=models.TextField()
    antxt=models.TextField()
    date=models.DateTimeField()

    def __str__(self):
        return self.antxt

       
    




