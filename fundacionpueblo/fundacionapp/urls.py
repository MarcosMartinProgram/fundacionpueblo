from django.urls import path 

from fundacionapp import views

urlpatterns = [
    
    path('', views.home, name='Home'),
    path('somos', views.somos, name='Quienes Somos'),
    path('blog', views.blog, name='Blog'),
    path('eventos', views.eventos, name='Eventos'),
    path('contacto', views.contacto, name='Contacto'),
    
    
]