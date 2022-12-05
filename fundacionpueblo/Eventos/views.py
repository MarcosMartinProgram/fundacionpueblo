from django.shortcuts import render

from Eventos.models import Eventos

# Create your views here.

def eventos(request):
    eventos=Eventos.objects.all()

    return render(request, 'Eventos/eventos.html', {'eventos': eventos});