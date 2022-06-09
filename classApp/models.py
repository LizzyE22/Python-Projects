from django.db import models

# Create your models here.


class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, default='')
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=60, default='')
    Duration = models.FloatField()


    objects = models.Manager()

    def __str__(self):
        return self.Title