from django.shortcuts import render, redirect
from .models import Principal, Predictivo, Campo_modelo, PersonalData
from django.views.generic import ListView, FormView
import pickle
from .ml_model import ml_heartAttack
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.
def heartAttack(request):
    principal = Principal.objects.get(id=3)
    return render(request, 'heartAttack.html', {'principal':principal})

def getValue(request):
    valores = request.POST.getlist('valores')
    valores = list(map(int, valores))
    y_Pred = ml_heartAttack(valores)
    Predictivo.objects.create(name=y_Pred.t_result())
    return redirect('/heart_attack/#pie-chart')

def envioMessage(request):
    if request.method == 'POST':
        name = request.POST('Name')
        email = request.POST('Email')
        message = request.POST('Message')

        template = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'message': message
        })

        email = EmailMessage(
            template,
            settings.EMAIL_HOST_USER,
            ['guillenpablo@gmail.com']
        )

        email.fail_silently = False
        email.send()

        message.success(request, 'Email sent successfully')
        return redirect('/')


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