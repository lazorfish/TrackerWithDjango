from django.db import models

# Create your models here.
class Project(models.Model):
    projectnumber = models.CharField(max_length=200, primary_key=True)
    company = models.CharField(max_length = 200)
    projectyear = models.CharField(max_length = 10)
class StartStopTimeEntry(models.Model):
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    project = models.ManyToManyField(Project)


class DurationTimeEntry(models.Model):
    duration = models.DateTimeField()
    project = models.DateTimeField()





