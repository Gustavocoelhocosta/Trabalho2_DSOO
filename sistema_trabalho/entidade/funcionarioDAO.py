from sistema_trabalho.entidade.DAO import DAO
from sistema_trabalho.entidade.funcionario import Funcionario
import pickle

class FuncionarioDAO(DAO):
    def __init__(self):
        super().__init__('funcionarios.pkl')

    def salvar(self, funcionario: Funcionario):
        if isinstance(funcionario, Funcionario) and funcionario is not None:
            super().salvar(funcionario.matricula, funcionario)

    def chamar(self, matricula):
        return super().chamar(matricula)

    def excluir(self, matricula):
        return super().remover(matricula)