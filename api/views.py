from django.shortcuts import render
from .serializers import ArticleSerializerList, ArticleSerializerDetail
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser
from .models import ArticleApi


#api for create and see the list of articles
class ArticleCreateList(ListCreateAPIView):
    queryset = ArticleApi.objects.all()
    serializer_class = ArticleSerializerDetail
    permission_classes = [IsAdminUser]

# api for list of articles
class ArticleList(ListAPIView):
    queryset = ArticleApi.objects.filter(status=True)
    serializer_class = ArticleSerializerList
    
# api for show detail of each article
class ArticleDetail(RetrieveAPIView):
    queryset = ArticleApi.objects.filter(status=True)
    serializer_class = ArticleSerializerDetail    
