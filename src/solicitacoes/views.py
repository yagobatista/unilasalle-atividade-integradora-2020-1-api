from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from solicitacoes.models import Solicitacao, Usuario, AtribuicaoTecnico, Tecnico
from solicitacoes.serializers import SolicitacaoSerializer, UsuarioSerializer, TecnicoSerializer
from rest_framework.response import Response


class SolicitacaoViewSet(ModelViewSet):
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer

    @action(detail=True, methods=['post'])
    def atribuir(self, request, pk):
        instance = self.get_object()
        tecnico = request.data.get('tecnico')
        AtribuicaoTecnico.objects.create(
            solicitacao=instance,
            tecnico_id=tecnico,
        )
        instance.refresh_from_db()
        serializer = self.serializer_class(
            instance=instance,
            expand=['usuario', 'atribuicoes_Tecnicos.tecnico'],
        )
        return Response(serializer.data)


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class TecnicoViewSet(ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer
    filterset_fields = ['email']

