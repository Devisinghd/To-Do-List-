from django.db import models
from django.utils.timezone import datetime
# Create your models here.
class Jobs(models.Model):

    task = models.CharField(max_length=50)
    description =models.TextField(max_length=100)
    time = models.TimeField()
    is_completed = models.BooleanField()


    def __str__(self):
        return self.task