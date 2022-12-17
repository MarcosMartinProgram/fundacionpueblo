from django.shortcuts import render, redirect
from .forms import formulariocontacto
from django.core.mail import EmailMessage


# Create your views here.

def contacto(request):
    formulario_contacto=formulariocontacto()
    if request.method=="POST":
        formulario_contacto=formulariocontacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde el Formulario de la Página", "El usuario con Nombre: {} con email {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido), "", "", reply_to=[email])

            try: 
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")



    return render(request, 'contacto/contacto.html', {'miformulario': formulario_contacto});