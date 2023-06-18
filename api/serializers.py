from .models import ArticleApi , DoctorProfile
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

#doctor profile list
class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = ['name', 'family' , 'expertise']

#doctor profile detail + create
class DoctorProfileDetail(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = '__all__'