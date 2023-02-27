
from attr import field
from django.core.paginator import Paginator
from django.db.models.base import Model
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import  MainModel, NewsLater , Category, Tag
from .forms import NewsLatterForm, SignUp
from django.views.generic.edit import FormView
from django.db.models import Q

#news form 
class Form(FormView):
    form_class = NewsLatterForm


    def Form(request):
        form = NewsLatterForm()
        if request.method == 'POST':
            form = NewsLatterForm(request.POST)
            if form.is_valid():
                form.save()
        context = {'form' : form}
        return render(request ,  'main/index.html' ,  context)
class Main(ListView):
    queryset= MainModel.objects.filter(Q(status = 'p') | Q(status= 'x'))
    fields = '__all__'
    template_name = "main/home-2.html"
    context_object_name = 'blog_list'
    paginate_by = 10

#//TODO //SOLVE THE BUG FOR SignUp FORM 

# signUp view 
class SignUp(FormView):
    form = SignUp()
    def signup(request):
        if request.method =='POST':
            form = SignUp(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = SignUp()
        return render(request, 'SignUp.html',{'fomr':form} )


class Review(ListView):
    model= MainModel
    fields = '__all__'
    template_name = "main/works.html"

class ReviewPC(ListView):
    model= MainModel
    fields = '__all__'
    template_name = "main/PC.html"

class ReviewSmartphone(ListView):
    model= MainModel
    fields = '__all__'
    template_name = "main/smartphone.html"

class ReviewLaptop(ListView):
    model= MainModel
    fields = '__all__'
    template_name = "main/laptop.html"

class ReviewSmartwatch(ListView):
    model= MainModel
    fields = '__all__'
    template_name = "main/smart-watch.html"

class Detail(DetailView):
    queryset= MainModel.objects.all()
    template_name='main/single.html'
    

    
    """def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context

        context = super().get_context_data(**kwargs)

        # Add in a QuerySet of all the books

        context['blog_list'] = MainModel.objects.all()

        return context"""

class CategoryList(ListView):
    paginate_by = 10
    template_name = 'main/category_list.html'
    context_object_name = "categoryes"
    def get_queryset(self):
        global category
        slug= self.kwargs.get('slug')
        category=get_object_or_404(Category,slug=slug)
        return category.articles.all()



    def get_contex_data(self, **kwargs):
        context=super().get_contex_data(**kwargs)
        context['category']=category
        return context

# 404 page 

def error_404(request, exception):
    return render(request, 'main/404.html')


# tags view 
class TagaListView(ListView):
    model = Tag
    field = '__all__'
    context_object_name = 'tags'
    template_name = 'main/tag.html'