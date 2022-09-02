import pickle
import itertools

class ml_heartAttack:
    def __init__(self, f_datos):
        self.f_datos = f_datos

    def t_result(self):
        with open('D:\ClasesPython\Django\predictML\principal\modelforrest_pickle','rb') as f:
            mod = pickle.load(f)
        with open('D:\ClasesPython\Django\predictML\principal\model_scaler','rb') as f:
            scaler = pickle.load(f)
        valores_transform = scaler.transform([self.f_datos])
        t_result = mod.predict_proba(valores_transform)
        t_result = list(itertools.chain.from_iterable(t_result))
        t_result = [i*100 for i in t_result]
        #t_result = t_result[0,1]
        return t_result