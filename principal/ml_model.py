import pickle
import itertools
from .models import Principal
from django.shortcuts import render
from django.templatetags.static import static
from django.conf import settings
import os

def open_model(file_name):
    models_folder = settings.BASE_DIR
    file_path = os.path.join(models_folder, os.path.basename(file_name))
    model = pickle.load(open(file_path, "rb"))
    return model

class ml_heartAttack:
    def __init__(self, f_datos):
        self.f_datos = f_datos

    def t_result(self):
        bb = (static('img/modelforrest_pickle'), 'rb')
        #with open(bb,'rb') as f:
        mod = open_model('modelforrest_pickle')
        #with open(static('/img/model_scaler'),'rb') as f:
        scaler = open_model('model_scaler')
        valores_transform = scaler.transform([self.f_datos])
        t_result = mod.predict_proba(valores_transform)
        t_result = list(itertools.chain.from_iterable(t_result))
        t_result = [i*100 for i in t_result]
        return t_result