from django.db import models
from django.utils import timezone

#article api model
class ArticleApi(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)
    #published_by = 
    
    def __str__(self):
        return self.title

#doctor profile 
class DoctorProfile(models.Model):
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=50)
    expertise = models.CharField(max_length=20)
    about_dr = models.TextField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.family