from typing import List
from django.db import models
from django.shortcuts import render
#login requierd decorators
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin 
#CLASS BASE VIEW
from django.views.generic import ListView , CreateView,UpdateView , DeleteView
#  for editing view
from django.urls import reverse_lazy

#import model article
from main.models import MainModel

class ArticleList(LoginRequiredMixin, ListView):
    queryset=MainModel.objects.all()
    template_name="registration/home.html"
# for creating article 
class ArticleCreate(LoginRequiredMixin, CreateView):
    model = MainModel
    fields = ['auther',"title","slug","category","description","thumbnail","date","status"]

    template_name= "registration/article-create-update.html"
# for editing article
class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = MainModel
    fields = ['auther',"title","slug","category","description","thumbnail","date","status"]

    template_name= "registration/article-create-update.html"

# for deleting article
class ArticleDelete(DeleteView):
    model = MainModel
    success_url = reverse_lazy('account:home')  
    template_name= "registration/article_model_confirm_delete.html" 