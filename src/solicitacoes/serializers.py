from rest_flex_fields import FlexFieldsModelSerializer
from solicitacoes.models import Solicitacao, Usuario, AtribuicaoTecnico, Tecnico


class UsuarioSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class TecnicoSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'


class AtribuicaoTecnicoSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = AtribuicaoTecnico
        exclude = ['solicitacao']
        expandable_fields = {
            'tecnico': TecnicoSerializer,
        }


class SolicitacaoSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Solicitacao
        exclude = ['tecnicos']
        expandable_fields = {
            'usuario': UsuarioSerializer,
            'atribuicoes_Tecnicos': (AtribuicaoTecnicoSerializer, {'many': True}),
        }
