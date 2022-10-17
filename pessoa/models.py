from django.db import models

class Pessoa(models.Model):
    nome_completo = models.charfiel(max_length=256, null=True, blank=True)