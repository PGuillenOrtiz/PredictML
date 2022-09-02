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
    option = models.JSONField(null=True)
    n_campo = models.FloatField(null=True, blank=True)
    ml_model = models.CharField(max_length=30)

    def __str__(self):
        nadmin = self.name_campo+'--'+self.ml_model
        return nadmin

class Principal(models.Model):
    images = models.ImageField()
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    predictivo = models.ForeignKey(Predictivo,null=True,blank=True,on_delete=models.CASCADE)
    url = models.URLField(max_length=255, null=True)

    def __str__(self):
        return self.name

