from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    tx=models.CharField(max_length=300)
    date=models.DateField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User)
