from django.urls import path

urlpatterns = [
    path('',ListaPessoaView.as_view(), name='pessoa.index')
]