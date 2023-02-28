from django.contrib import admin

from main.views import Main
from .models import  MainModel , Category,NewsLater ,IPAdress, Tag , CommentModel

# comment admin 
class CommentInline(admin.StackedInline):
    model = CommentModel
    extra = 0

class From_admin(admin.ModelAdmin):
    list_display =['name', 'email']
admin.site.register(NewsLater,From_admin)
class Category_admin(admin.ModelAdmin):
    list_display=['title' ,'slug','description','status', 'parent']
admin.site.register(Category,Category_admin)

class Main_Admin(admin.ModelAdmin):
    list_display = ['title', 'status', 'category_to_str' , 'slug' , 'date' ]
    inlines = [
        CommentInline,
    ]
    def category_to_str(self, obj):
        return ", ".join([category.title for category in  obj.category.all()])
    category_to_str.short_description = "category"

    """def tag_to_str(self, obj):
        return b" ".join([Tag.title for tags in  obj.tags.all()])
    tag_to_str.short_description = "tags"""
admin.site.register(MainModel,Main_Admin)

admin.site.register(IPAdress)
admin.site.register(Tag)