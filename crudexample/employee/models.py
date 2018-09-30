from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    eFirstName = models.CharField(max_length=100)
    eLastName = models.CharField(max_length=100)
    dId = models.CharField(max_length=15)

    def __str__(self):
        return '%s %s %s' % (self.eFirstName, self.eLastName,self.dId)