from email.mime import image
from ipaddress import ip_address
import time 
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#اضافه کردن  ادیتور سی کی به پروژه 
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields  import RichTextField
#from matplotlib.pyplot import title

# jalali 
from extensions.utils import jalali_convertor

from django.urls import reverse


from PIL import Image
from os import path

from django.urls import reverse


#manager model 
class ArticleManager(models.Manager):
	def published(self):
		return self.filter(status='p')



    
class Category(models.Model):
    title=models.CharField(max_length=100, verbose_name="title")
    slug=models.CharField(max_length=50,verbose_name="url")
    description=models.CharField(max_length=500, verbose_name="desciption")
    status=models.BooleanField(default=True ,verbose_name="status")
    parent = models.ForeignKey('self', default=None , on_delete=models.SET_NULL , null=True, blank = True,verbose_name='دسته اصلی' , related_name='children')

    class Meta:
            verbose_name="category "
            verbose_name_plural="categorys"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
		    return reverse('main:category' , args = [self.slug,])

class IPAdress(models.Model):
    ip_address=models.GenericIPAddressField(verbose_name='آیپی ها')

    def __str__(self):
        return self.ip_address
        
# tags model
class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان ')
    description = models.TextField(max_length=100 ,verbose_name='توضیحات')
    slug = models.SlugField(max_length=50 ,verbose_name='آدرس')
    published = models.DateTimeField(default=timezone.now ,verbose_name='زمان انتشار ')
    status = models.BooleanField(default=True , verbose_name='وضعیت ')

    def __str__(self):
        return self.title

class UserReqester(models.Model):
    username = models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    email = models.EmailField(null=True)
    


#Main model 
class MainModel(models.Model):
        STATUS_CHOICES=(
        ('p' , 'blog'),
        (' d ' , 'DRAFT'),
        #big slider
        ('x' , 'slider'),
        #top blog
        #('y' , 'پین کردن'),
        )
        auther=models.ForeignKey(User, null=True, on_delete=models.SET_NULL,verbose_name="auther")
        title=models.CharField(max_length=100 ,  verbose_name="title" ,null="False")
        slug=models.SlugField(max_length=50, verbose_name="url" ,null="False")
        thumbnail=models.ImageField(upload_to="images",verbose_name="picture-url" ,null="True")
        category=models.ManyToManyField(Category,verbose_name="category",related_name="articles")
        #description=models.TextField(max_length=500, verbose_name="description")
        description =RichTextField(blank="True", null="True")
        description =RichTextUploadingField(blank="True", null="True")
        thumbnail=models.ImageField(upload_to="images",verbose_name="picture-url" ,null="True")
        date=models.DateTimeField(default=timezone.now)
        status=models.CharField(max_length=3,choices=STATUS_CHOICES , verbose_name="status",null="False")
        tags = models.ManyToManyField(Tag, null = True , blank= True ,  related_name='tags' , verbose_name=' برچسب')

        """def save(self, *args, **kwargs):
            super(MainModel, self).save(*args, **kwargs)
            imag = Image.open(self.description.path)
            if imag.width > 400 or imag.height> 300:
                output_size = (400, 300)
                imag.thumbnail(output_size)
                imag.save(self.description.path)"""

        class Meta:
            verbose_name="Main "
            verbose_name_plural="Mains"
            ordering=['-date']

        def __str__(self):
            return self.title
        

        def jpublish(self):
            return jalali_convertor(self.date)

        def get_absolute_url(self):
		        return reverse('main:detail' , args = [self.slug,])
			



#submit form [sidebar]
class NewsLater(models.Model):
    name= models.CharField(max_length=150)
    email= models.EmailField()
    publish = models.DateTimeField(default=timezone.now)

objects = ArticleManager()

# Comment model 
class CommentModel(models.Model):
    post = models.ForeignKey(MainModel,
                            on_delete=models.CASCADE,
                            related_name='comments' , null=True)
    name = models.CharField(max_length= 100)
    email = models.EmailField()
    comment = models.TextField(max_length=600)
    created = models.DateTimeField(auto_now_add=True , null=True) 
    updated = models.DateTimeField(auto_now=True , null=True) 
    active = models.BooleanField(default=True , null=True) 


    """class Meta:
        ordering = ['created_on']"""

    def __str__(self):
        return self.comment[:60]