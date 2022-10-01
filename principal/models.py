from django.db import models

# Create your models here.
class Predictivo(models.Model):
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'Predictivo'
        verbose_name_plural = 'Predictivos'
        db_table = 'predictivo'

class Campo_modelo(models.Model):
    name_campo = models.CharField(max_length=30)
    info = models.TextField(max_length=255)
    option = models.JSONField(null=True, blank=True)
    n_campo = models.FloatField(null=True, blank=True)
    ml_model = models.CharField(max_length=30)

    def __str__(self):
        nadmin = self.name_campo+'--'+self.ml_model
        return nadmin

class Principal(models.Model):
    images = models.TextField(max_length=255)
    name = models.CharField(max_length=30)
    partial_description = models.TextField(max_length=255)
    full_description = models.TextField(max_length=2000, null=True)
    predictivo = models.ForeignKey(Predictivo,null=True,blank=True,on_delete=models.CASCADE)
    url = models.CharField(max_length=255, null=True, blank=True)
    notebook_model = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

class PersonalData(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    email = models.EmailField(max_length=40)
    address = models.TextField(max_length=255)
    telefone = models.TextField(max_length=100)
    curriculum = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
