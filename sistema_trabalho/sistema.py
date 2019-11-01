from sistema_trabalho.limite.telaInicial import TelaInicial
from sistema_trabalho.controle.controlaEmprestimo import ControlaEmprestimo
from sistema_trabalho.controle.controlaFuncionario import ControlaFuncionario
from sistema_trabalho.controle.controlaVeiculo import ControlaVeiculo
from sistema_trabalho.entidade.veiculo import Veiculo
from sistema_trabalho.entidade.funcionario import Funcionario
from sistema_trabalho.entidade.registro import Registro


class Sistema():
    def __init__(self):
        self.__tela_inicial = TelaInicial()

        self.__controla_veiculo = ControlaVeiculo(self)
        v0 = Veiculo('AAA0000', 'ONIX', 'CHEVROLET', 2000, 15000)
        v1 = Veiculo('BBB1111', 'X1', 'BMW', 2000, 15000)
        v2 = Veiculo('CCC2222', 'K', 'FORD', 2000, 15000)
        self.__controla_veiculo.veiculos['AAA0000'] = v0
        self.__controla_veiculo.veiculos['BBB1111'] = v1
        self.__controla_veiculo.veiculos['CCC2222'] = v2

        self.__controla_funcionario = ControlaFuncionario(self)
        f0 = Funcionario(0, 'JOÃO', '07061984', '48988041793', 'FUNCIONARIO')
        f1 = Funcionario(1, 'MARIA', '07061984', '48988041793', 'DIRETOR')
        f2 = Funcionario(2, 'JOSÉ', '07061984', '48988041793', 'OPERADOR')
        f3 = Funcionario(3, 'JOELMA', '07061984', '48988041793', 'OPERADOR')
        self.__controla_funcionario.funcionarios[0] = f0
        self.__controla_funcionario.funcionarios[1] = f1
        self.__controla_funcionario.funcionarios[2] = f2
        self.__controla_funcionario.funcionarios[3] = f3
        self.__controla_funcionario.funcionarios[0].veiculos['AAA0000'] = v0
        self.__controla_funcionario.funcionarios[0].veiculos['BBB1111'] = v1
        self.__controla_funcionario.funcionarios[2].veiculos['CCC2222'] = v2

        self.__controla_emprestimo = ControlaEmprestimo(self)
        r0 = Registro(v1,f1,0)
        r1 = Registro(v2,f1,1)
        r2 = Registro(v2,f2,2)
        r3 = Registro(v0,f0,3)
        r4 = Registro(v0,f3,4)
        r5 = Registro(v1,f0,0)
        self.__controla_emprestimo.registros.append(r0)
        self.__controla_emprestimo.registros.append(r1)
        self.__controla_emprestimo.registros.append(r2)
        self.__controla_emprestimo.registros.append(r3)
        self.__controla_emprestimo.registros.append(r4)
        self.__controla_emprestimo.registros.append(r5)

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
        opcoes = {0: self.chamar_controla_veiculo, 1: self.chamar_controla_funcionario, 2: self.chamar_controla_emprestimo}
        opcao = self.__tela_inicial.listar_opcoes_sistema()
        return opcoes[opcao]()

    def chamar_controla_veiculo(self):
        self.__controla_veiculo.abrir_tela()

    def chamar_controla_emprestimo(self):
        self.__controla_emprestimo.abrir_tela()

    def chamar_controla_funcionario(self):
        self.__controla_funcionario.abrir_tela()


s = Sistema()
s.chamar_tela_inicial()


