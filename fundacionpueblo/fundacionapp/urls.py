from django.urls import path 

from fundacionapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.home, name='Home'),
    path('somos', views.somos, name='Quienes Somos'),
    path('blog', views.blog, name='Blog'),
    path('contacto', views.contacto, name='Contacto'),
    
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 