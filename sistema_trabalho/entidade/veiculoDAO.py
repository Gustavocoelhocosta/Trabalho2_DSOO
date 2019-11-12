from sistema_trabalho.entidade.DAO import DAO
from sistema_trabalho.entidade.veiculo import Veiculo
import pickle


class Veiculo_DAO(DAO):
    def __init__(self):
        super().__init__('veiculos.pkl')

    def salvar(self, veiculo: Veiculo):
        if isinstance(veiculo,Veiculo) and veiculo is not None:
            super().salvar(veiculo.placa, veiculo)

    def chamar(self, placa):
        return super().chamar(placa)

    def excluir(self, placa):
        return super().remover(placa)