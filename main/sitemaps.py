from django.contrib import sitemaps
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Category,MainModel
class StaticSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return [
            'main:index', 
            
            ]

    def location(self, item):
        return reverse(item)

class CategorySitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Category.objects.all()

class DetailSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return MainModel.objects.all()