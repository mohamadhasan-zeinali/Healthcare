
from cgitb import handler
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#sitemap
# from django.contrib.sitemaps.views import sitemap
# from main.sitemaps import StaticSitemap , CategorySitemap , DetailSitemap

# sitemaps = {
    # 'static' : StaticSitemap,
    # 'category': CategorySitemap,
    # 'detail': DetailSitemap
# }
# 

#from main.views import Page404
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('main.urls')),
    #path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('account/',include('account.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        #  name='django.contrib.sitemaps.views.sitemap')
    #path('404/', include('main.urls'))
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

# handler404= 'main.views.error_404'
