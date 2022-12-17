from django.urls import path

from .views import  VistaLogin, cerrar_sesion, logear


urlpatterns = [    
        
    path('', VistaLogin.as_view(), name='Login'),    

    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),

    path('logear', logear, name='logear'),
]


