from .models import ArticleApi 
from rest_framework import serializers


# article serializer list 
class ArticleSerializerList(serializers.ModelSerializer):
    class Meta:
        model = ArticleApi
        fields = ('title',)   

#article serialier detail 
class ArticleSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = ArticleApi 
        fields = '__all__'    
