
from attr import field
from django.core.paginator import Paginator
from django.db.models.base import Model
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import  MainModel, Category, Tag
from .forms import  SearchForm, CommentForm
from django.views.generic.edit import FormView
from django.db.models import Q
import requests

#news form 
"""class Form(FormView):
    form_class = NewsLatterForm


    def Form(request):
        form = NewsLatterForm()
        if request.method == 'POST':
            form = NewsLatterForm(request.POST)
            if form.is_valid():
                form.save()
        context = {'form' : form}
        return render(request ,  'main/index.html' ,  context)"""
    

class Main(ListView):
    queryset= MainModel.objects.filter(Q(status = 'p') | Q(status= 'x'))
    fields = '__all__'
    template_name = "main/home-2.html"
    context_object_name = 'blog_list'
    paginate_by = 10
"""    model = MainModel
    def get_queryset(self):
        person = MainModel.objects.all()
        #name = self.kwargs.get('title',)
        #object_list = self.model.objects.all()
        form = SearchForm()
        if 'search' in request.GET: 
            form = SearchForm(request.GET)
            if form.is_valid():
                cd = form.cleaned_data('search')
                person = person.filter(title=cd)
        return render(request,{'person':person, 'fomr':form})"""
            


#//TODO //SOLVE THE BUG FOR SignUp FORM 

# signUp view 
"""class SignUp(FormView):
    form = SignUp()
    def signup(request):
        if request.method =='POST':
            form = SignUp(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = SignUp()
        return render(request, 'SignUp.html',{'fomr':form} )"""


class Review(ListView):
    model= MainModel
    fields = '__all__'
    template_name = "main/works.html"

class PostDetailView(DetailView):

    def get(self, request, *args, **kwargs):
        view = Detail.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = Detail.as_view()
        return view(request, *args, **kwargs)

class Detail(DetailView):
    model = MainModel
    template_name='main/single.html'
    context_object_name= 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
 
#post comment 
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from .forms import CommentForm

class PostComment(SingleObjectMixin, FormView):
    model = MainModel
    form_class = CommentForm
    template_name = 'main/single.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse('post_detail', kwargs={'pk': post.pk}) + '#comments'
    
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