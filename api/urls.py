from django.urls import path
from .views import (
    ArticleCreateList,
    ArticleList,
    ArticleDetail, 
    DoctorProfileView,
    DoctorsCreateProfileView, 
    DoctorsDetailPage,
)
app_name="api"

urlpatterns =[
    path('blog/', ArticleList.as_view(), name = 'article_list'), # article api list url
    path('blog/create/', ArticleCreateList.as_view(), name= 'create_article'), #article create-list api url
    path('blog/<int:pk>/', ArticleDetail.as_view(), name = 'article_detail'), #article details api url
    path('doctors/',DoctorProfileView.as_view(), name='DoctorProfile'), #doctors list / profile api url
    path('doctors/create/', DoctorsCreateProfileView.as_view(), name='doctors_detail'), #doctors profile detail
    path('doctors/<int:pk>/', DoctorsDetailPage.as_view(), name='doctors_detail_page'), #doctors profile page url

]