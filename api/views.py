from django.shortcuts import render
from .serializers import (
    ArticleSerializerList,
    ArticleSerializerDetail,
    DoctorProfileSerializer,
    DoctorProfileDetail,
)
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser
from .models import ArticleApi, DoctorProfile


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

#api for list of doctors
class DoctorProfileView(ListAPIView):
    queryset = DoctorProfile.objects.filter(status = True)
    serializer_class = DoctorProfileSerializer

#‌class Doctors create profile
class DoctorsCreateProfileView(ListCreateAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileDetail
    permission_classes = [IsAdminUser]

# api for show detail  profile of each doctors
class DoctorsDetailPage(RetrieveAPIView):
    queryset = DoctorProfile.objects.filter(status=True)
    serializer_class = DoctorProfileDetail   
