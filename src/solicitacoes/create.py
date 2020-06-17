from django.utils.timezone import localtime

from solicitacoes.models import *

Tecnico.objects.create(email='funcionario2@empresa.com.br',
                      nome='funcionario 2', senha='12qwas', departamento='ti')
Tecnico.objects.all()
# AtribuicaoTecnico.objects.create(
#     tecnico_id=1,
#     solicitacao_id=2,
#     horario=localtime(),
# )