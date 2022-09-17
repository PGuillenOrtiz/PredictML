from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import Principal, Predictivo, Campo_modelo, PersonalData
from django.views.generic import ListView, FormView
import pickle
from .ml_model import ml_heartAttack
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

# Create your views here.
def stellar_class(request):
    stellar_bd = Principal.objects.get(name="Stellar Classification")
    return render(request, 'stellar_class.html', {'principal':stellar_bd})

def getValue(request):
    valores = request.POST.getlist('valores')
    valores = list(map(int, valores))
    y_Pred = ml_heartAttack(valores)
    Predictivo.objects.create(name=y_Pred.t_result())
    return redirect('/heart_attack/#pie-chart')

def envioMessage(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST['email']
        message = request.POST['Message']
        subject = 'Mensaje de la pagina MLPredict de '+name

        template = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'message': message
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['guillenpablo@gmail.com']
        )

        email.fail_silently = False
        email.send()

        messages.success(request, 'Email sent successfully')
        url = request.META['HTTP_REFERER']
        print(url)
        return redirect(url + '#contact')


class HA_FormListView(ListView):
    model = Campo_modelo
    template_name = 'heartAttack.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['principal'] = Principal.objects.get(name="Heart Disease")
        context['personal'] = PersonalData.objects.get(name='Pablo Guillen Ortiz')
        context['cv'] = Principal.objects.get(name="Heart Disease")
        try:
            valor = Predictivo.objects.all()[0]
            context['result1'] = valor
            valor.delete()
        except Exception:
            context['result1'] = ''
        return context

class PrincipalListView(ListView):
    model = Principal
    template_name = 'principal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(context)
        context['post'] = Predictivo.objects.filter(name='lacree')
        context['personal'] = PersonalData.objects.get(name='Pablo Guillen Ortiz')
        context['cv'] = Principal.objects.get(name="Heart Disease")
        return context