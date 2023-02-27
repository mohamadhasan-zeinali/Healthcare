
from django import template
from ..models import MainModel,Category
register = template.Library()

#sidebar
@register.inclusion_tag('main/sidebar_left.html')
def Sidebar_left():
    return{
        'blog_list':MainModel.objects.all()
    }

@register.inclusion_tag('main/sidebar_right.html')
def Sidebar_right():
    return{
        'sidebar_right':Category.objects.all()
    }

#navbar
@register.inclusion_tag('main/navbar.html')
def Navbar():
    return{
        'navbar':Category.objects.all()
    }