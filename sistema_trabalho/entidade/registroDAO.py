from sistema_trabalho.entidade.DAO import DAO
from sistema_trabalho.entidade.registro import Registro


class Registro_DAO(DAO):
    def __init__(self):
        super().__init__('registros.pkl')

    def salvar(self, registro: Registro):
        if isinstance(registro,Registro) and registro is not None:
            super().salvar(registro.veiculo.placa, registro)

    def chamar(self, placa):
        return super().chamar(placa)

    def excluir(self, placa):
        return super().remover(placa)