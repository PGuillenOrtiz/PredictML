from django.shortcuts import render, redirect
from .models import Principal, Predictivo, Campo_modelo
from django.views.generic import ListView, FormView
import pickle
from .ml_model import ml_heartAttack

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

def el_valor():
    a=0
    return a


def HA_FormView(request):
    principal = Campo_modelo.objects.all
    return render(request, 'heartAttack.html', {'principal':principal})

def principal(request):
    principal = 3
    return render(request, 'heartAttack.html', {'principal':principal})

def sum():
    a=1
    b=2
    return a+b

class HA_FormListView(ListView):
    model = Campo_modelo
    template_name = 'heartAttack.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['principal'] = Principal.objects.get(id=3)
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
        context['jose'] = sum()
        return context