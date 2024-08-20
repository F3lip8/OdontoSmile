from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

SERVICOS = (
    ("restauração","Restauração"),
    ("implantes","Implantes"),
    ("limpeza","Limpeza"),
    ("exodontia","Exodontia"),
    ("coroa","Coroa"),
    ("facetas","Facetas"),
    ("lentes de contato","Lentes de contato"),
    ("ortodontia","Ortodontia"),
)

HORARIOS = (
    ("oito","08:00"),
    ("09:00", "09:00"),
    ("dez","10:00"),
    ("onze","11:00"),
    ("duas","14:00"),
    ("tres","15:00"),
    ("quatro","16:00"),
    ("cinco","17:00"),
)

class Consulta(models.Model):
    cpf = models.DecimalField(max_digits=11, decimal_places=0)
    nome_do_paciente = models.CharField(max_length=50, help_text="Nome do paciente")
    serviço = models.CharField(choices=SERVICOS, max_length=50)
    data = models.DateField(blank=True, null=True)
    hora = models.CharField(choices=HORARIOS, max_length=50, null=True)
    dentista = models.ForeignKey('Dentista', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome_do_paciente

    def get_absolute_url(self):
        return reverse('Detalhes-consulta', args=[str(self.id)])


class Dentista(models.Model):
    nome_do_dentista = models.CharField(max_length=50)
    CRO = models.DecimalField(max_digits=11, decimal_places=0)

    def __str__(self):
        return self.nome_do_dentista
