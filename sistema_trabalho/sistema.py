from sistema_trabalho.limite.telaInicial import TelaInicial
from sistema_trabalho.controle.controlaEmprestimo import ControlaEmprestimo
from sistema_trabalho.controle.controlaFuncionario import ControlaFuncionario
from sistema_trabalho.controle.controlaVeiculo import ControlaVeiculo

class Sistema():
    def __init__(self):
        self.__tela_inicial = TelaInicial()
        self.__controla_veiculo = ControlaVeiculo(self)
        self.__controla_funcionario = ControlaFuncionario(self)
        self.__controla_emprestimo = ControlaEmprestimo(self)

    @property
    def tela_inicial(self):
        return self.__tela_inicial

    @property
    def controla_veiculo(self):
        return self.__controla_veiculo

    @property
    def controla_emprestimo(self):
        return self.__controla_emprestimo

    @property
    def controla_funcionario(self):
        return self.__controla_funcionario

    def chamar_tela_inicial(self):
        opcoes = {0: self.chamar_controla_veiculo, 1: self.chamar_controla_funcionario, 2: self.chamar_controla_emprestimo, None: self.finalizar}
        botao, valores = self.__tela_inicial.abrir()
        return opcoes[botao]()

    def chamar_controla_veiculo(self):
        self.__controla_veiculo.abrir_tela()

    def chamar_controla_emprestimo(self):
        self.__controla_emprestimo.abrir_tela()

    def chamar_controla_funcionario(self):
        self.__controla_funcionario.abrir_tela()

    def finalizar(self):
        return exit(0)


s = Sistema()
s.chamar_tela_inicial()


