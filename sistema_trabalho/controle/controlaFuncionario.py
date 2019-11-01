from sistema_trabalho.limite.telaFuncionario import TelaFuncionario
from sistema_trabalho.entidade.funcionario import Funcionario
from sistema_trabalho.controle.controlaAbstract import ControlaAbstract

class ControlaFuncionario(ControlaAbstract):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__funcionarios = dict()
        self.__tela = TelaFuncionario()

    @property
    def funcionarios(self):
        return self.__funcionarios

    def abrir_tela(self):
        self.__tela.imprimir('----------------------------------------------------')
        opcoes = {0: self.incluir,
                  1: self.excluir,
                  2: self.listar,
                  3: self.cadastrar_veiculo_no_funcionario,
                  4: self.excluir_veiculo_do_funcionario,
                  5: self.listar_veiculos_permitidos,
                  6: self.voltar}
        opcao = self.__tela.listar_opcoes()
        opcoes[opcao]()
        return self.abrir_tela()

    def incluir(self):
        dados_funcionario = self.__tela.cadastrar_funcionario()
        matricula = dados_funcionario[0]
        nome = dados_funcionario[1]
        data_de_nascimento = dados_funcionario[2]
        telefone = dados_funcionario[3]
        cargo = dados_funcionario[4]

        if matricula in self.__funcionarios:
            self.__tela.imprimir('Não foi possivel cadastrar pois já existe um funcionário com essa matrícula')
        else:
            self.__funcionarios[matricula] = Funcionario(matricula, nome, data_de_nascimento, telefone, cargo)
            self.__tela.imprimir('Funcionário cadastrado com sucesso!')

    def excluir(self):
        funcionarios = self.__funcionarios
        for funcionario in funcionarios:
            print('%s - %s' % (funcionarios[funcionario].matricula, funcionarios[funcionario].nome))
        matricula = self.__tela.pedir_matricula()
        if matricula in self.__funcionarios:
            del (self.__funcionarios[matricula])
            self.__tela.imprimir('Funcionário exclído com sucesso')
        else:
            self.__tela.imprimir('Não foi possível excluir, matrícula inválida')

    def listar(self):
        self.__tela.listar_funcionarios(self.__funcionarios)

    def cadastrar_veiculo_no_funcionario(self):
        self.__tela.imprimir('Cadastrando um veículo no funcionário')
        funcionarios = self.__funcionarios
        for funcionario in funcionarios:
            self.__tela.imprimir('%s - %s' % (funcionarios[funcionario].matricula, funcionarios[funcionario].nome))
        matricula = self.__tela.pedir_matricula()
        while not matricula in funcionarios:
            matricula = self.__tela.pedir_matricula()
        veiculos = self.__sistema.controla_veiculo.veiculos
        for veiculo in veiculos:
            self.__tela.imprimir('%s - %s' % (veiculos[veiculo].placa, veiculos[veiculo].modelo))
        placa = self.__tela.pedir_placa()
        carro = veiculos[placa]
        funcionarios[matricula].veiculos[placa] = carro
        self.__tela.imprimir('Veículo cadastrado com sucesso')

    def excluir_veiculo_funcionarios(self, placa):
        for funcionario in self.__funcionarios.values():
            funcionario.excluir_veiculo(placa)

    def excluir_veiculo_do_funcionario(self):
        self.__tela.imprimir('Excluíndo veículo da lista do funcionário')
        funcionarios = self.__funcionarios
        self.listar()
        matricula = self.__tela.pedir_matricula()
        while not matricula in funcionarios:
            matricula = self.__tela.pedir_matricula()
        veiculos = self.__funcionarios[matricula].veiculos
        if len(veiculos) > 0:
            for veiculo in veiculos:
                self.__tela.imprimir('%s - %s' % (veiculos[veiculo].placa, veiculos[veiculo].modelo))
            placa = self.__tela.pedir_placa()
            del funcionarios[matricula].veiculos[placa]
            self.__tela.imprimir('Veículo removido da lista de veículos permitidos')
        else:
            self.__tela.imprimir('O funcionário não tem nenhum veículo cadastrado')

    def listar_veiculos_permitidos(self):
        funcionarios = self.__funcionarios
        self.listar()
        self.__tela.imprimir('----------------------------------------------------')
        matricula = self.__tela.pedir_matricula()
        while not matricula in funcionarios:
            matricula = self.__tela.pedir_matricula()
        veiculos_permitidos = funcionarios[matricula].veiculos
        if not len(veiculos_permitidos) == 0:
            self.__tela.imprimir('O funcionário tem permissão para os seguintes carros: ')
            for veiculo in veiculos_permitidos:
                self.__tela.imprimir('%s - %s' % (veiculos_permitidos[veiculo].placa, veiculos_permitidos[veiculo].modelo))
        else:
            self.__tela.imprimir('Nenhum vaículo cadastrado para esse funcionário')

    def buscar_funcionario_matricula(self, matricula):
        if matricula in self.__funcionarios:
            return self.__funcionarios[matricula]
        else:
            return None

    def voltar(self):
        self.__sistema.chamar_tela_inicial()