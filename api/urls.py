from django.urls import path
from .views import ArticleCreateList ,ArticleList,ArticleDetail
app_name="api"

urlpatterns =[
    path('', ArticleList.as_view(), name = 'article_list'), # article api list url
    path('create/', ArticleCreateList.as_view(), name= 'create_article'), #article create-list api url
    path('blog/<int:pk>/', ArticleDetail.as_view(), name = 'article_detail'), #article details api url
]