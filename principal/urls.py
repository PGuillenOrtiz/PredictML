from django.urls import path
from . import views
from .views import heartAttack, getValue

urlpatterns = [
    path('', views.PrincipalListView.as_view(), name='PrincipalListView'),
    path('heart_attack/', views.HA_FormListView.as_view(), name='HA_FormListView'),
    path('getValue/', getValue),
]