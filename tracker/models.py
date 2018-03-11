from django.db import models

# Create your models here.
class TimeEntry(models.Model):
    date_and_time = models.DateTimeField()
    project = models.ForeignKey(Project)

class Project(models.Model):
    company = models.CharField(max = 200)
    


