from email.policy import default
from django.db import models

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=256, null=True, blank=True)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True) 
    