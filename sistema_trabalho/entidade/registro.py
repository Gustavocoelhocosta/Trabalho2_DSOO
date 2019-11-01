from sistema_trabalho.entidade.funcionario import Funcionario
from sistema_trabalho.entidade.veiculo import Veiculo
import datetime

class Registro():
    def __init__(self, veiculo: Veiculo, funcionario: Funcionario, motivo: int):
        self.__veiculo = veiculo
        self.__funcionario = funcionario
        self.__data_hora = datetime.datetime.now()
        self.__motivos = ['Acesso permitido ao veiculo', 'Matrícula não existe', 'Não possui acesso ao veículo', 'veículo indisponível', 'Acesso Bloqueado']
        self.__motivo = self.__motivos[motivo]

    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def funcionario(self):
        return self.__funcionario

    @property
    def data_hora(self):
        return self.__data_hora

    @property
    def motivo(self):
        return self.__motivo

    @property
    def motivos(self):
        return self.motivos