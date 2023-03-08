from django.contrib.auth import views
from django.urls import path
from .views import (
    ArticleList ,
    ArticleCreate,
    ArticleUpdate,
    ArticleDelete
    )

app_name="account"
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),


]
urlpatterns += [
    path('', ArticleList.as_view(), name='home'),
    path('article/create', ArticleCreate.as_view(), name='article-create'),#برای ساخت وبلاگ
    path('article/update/<int:pk>', ArticleUpdate.as_view(), name='article-update'),#ویو اپدیت
     path('article/delete/<int:pk>', ArticleDelete.as_view(), name='article-delete'),#ویو دیلت
]