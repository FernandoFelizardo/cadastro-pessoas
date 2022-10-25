from django.contrib import admin

from pessoa.models import Pessoa

# Registrar aqui para aparecer na tela do admin
admin.site.register(Pessoa)


class PessoaAdmin (admin.ModelAdmin):
    pass
