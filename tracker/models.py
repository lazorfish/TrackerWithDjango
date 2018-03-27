from django.db import models

# Create your models here.
class StartStopTimeEntry(models.Model):
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    project = models.ManytoManyField(Project)


class DurationTimeEntry(models.Model):
    duration = models.DateTimeField()
    project = models.DateTimeField()

class Project(models.Model):
    projectnumber = models.CharField(max=200, primary_key=True)
    company = models.CharField(max = 200)
    projectyear = models.CharField(max = 10)



