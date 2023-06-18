from django.db import models
from django.utils import timezone
# Create your models here.
class ArticleApi(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)
    #published_by = 