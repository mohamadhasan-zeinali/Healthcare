from django.urls import path
from .views import (
        Main,
        Review,
        Detail,
        ReviewLaptop,
        ReviewSmartphone,
        ReviewPC,
        ReviewSmartwatch,
        CategoryList,
        #Page404, 
        TagaListView, 
        SignUp
)

app_name="main"

urlpatterns =[
    path('',Main.as_view(), name="index" ),
    path('reviews/',Review.as_view(), name="reviews"),
    #path('404/', Page404.as_view(), name="404"),

    path('category/<slug:slug>',CategoryList.as_view(), name="category"),
    path('category/<slug:slug>/page/<int:page>',CategoryList.as_view(), name="category"),

    path('tag/<slug:slug>',TagaListView.as_view(), name="tag"),
    path('tag/<slug:slug>/page/<int:page>',TagaListView.as_view(), name="tag"),
    path('signup/', SignUp.as_view(), name = 'signup'),

    #path('reviews/laptop/',ReviewLaptop.as_view(), name="laptop"),
    #path('reviews/smartphone/',ReviewSmartphone.as_view(), name="smart-phone"),
    #path('reviews/pc/',ReviewPC.as_view(), name="pc"),
    #path('reviews/smartwatch/',ReviewSmartwatch.as_view(), name="smart-watch"),
    path('blog/<slug:slug>',Detail.as_view(), name="detail"),
]
    
