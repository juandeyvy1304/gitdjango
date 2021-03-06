from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'tituloIni':'lod saluda juandavid piedrahita', 'titulo2': 'clases de python'})   

class NosotrosPageView(TemplateView):
     
    template_name = "nosotros.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulous':'acerca de nosotros', 'descripcion':'somos'})

def Contacto(request):
    formcontact = ContactForm()


    # validar que el formulario tenga una peticion post
    if request.method == "POST":

        formcontact = ContactForm(data=request.POST)
        if formcontact.is_valid():
            tipomsj = request.POST.get('tipomsj', '')
            nombre = request.POST.get('nombre', '')
            correo = request.POST.get('correo', '')
            mensaje = request.POST.get('mensaje', '')

            #creamos el objeto con las variables del formulario
            email = EmailMessage(
                "RepoDevelopers: tienes un nuevo mensaje de contacto",
                "De: {} <{}>\n\nescribio:\n\nTipo de Mensaje:{}\n{}".format(nombre,correo,tipomsj,mensaje),
                "no-contestar@inbox.mailtrap.io",
                ["piedrahitarojasjuandavid@gmail.com"],
                reply_to[correo]
            )
            #enviamos el correo
            try:
                email.send()
                return redirect(reverse('contactanos')+"?ok")
            except:
                return redirect(reverse('contacto')+"?fail")


    return render(request, 'contactenos.html', {'formulario': formcontact})