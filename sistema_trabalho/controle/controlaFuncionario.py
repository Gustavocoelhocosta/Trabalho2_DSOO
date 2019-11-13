from sistema_trabalho.limite.Telas_funcionario.telaListaFuncionario import TelaListaFuncionario
from sistema_trabalho.limite.Telas_funcionario.telaCadastraFuncionario import TelaIncluirFuncionario
from sistema_trabalho.entidade.funcionario import Funcionario
from sistema_trabalho.entidade.funcionarioDAO import FuncionarioDAO
from sistema_trabalho.controle.controlaAbstract import ControlaAbstract

class ControlaFuncionario(ControlaAbstract):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__funcionario_DAO = FuncionarioDAO()
        self.__tela_listar_funcionarios = TelaListaFuncionario()
        self.__tela_cadastrar_funcionario = TelaIncluirFuncionario()
        self.__cargos = ['Administrativo', 'Direção', 'Operacional', 'TI']

    @property
    def funcionarios_DAO(self):
        return self.__funcionario_DAO

    def abrir_tela(self):
        funcionarios = list()
        for funcionario in self.__funcionario_DAO.chamar_todos():
            funcionarios.append(
                str(funcionario.matricula) + ' - ' +
                funcionario.nome + ' - ' +
                str(funcionario.data_de_nascimento) + ' - ' +
                str(funcionario.telefone) + ' - ' +
                funcionario.cargo
                )
        botoes, valores = self.__tela_listar_funcionarios.abrir(funcionarios)
        print(botoes, valores)
        opcoes = {'Novo': self.incluir,
                  'Excluir': self.excluir,
                  'Alterar': self.listar,
                  'Veículos permitidos': self.cadastrar_veiculo_no_funcionario,
                  'Voltar': self.voltar,
                  None: self.voltar}
        if botoes in ['Alterar', 'Excluir', 'Veículos permitidos']:
            opcoes[botoes](valores)
        else:
            opcoes[botoes]()
            self.abrir_tela()

    def incluir(self):
        botoes, dados_funcionario = self.__tela_cadastrar_funcionario.abrir(None, self.__cargos)
        print(botoes, dados_funcionario)
        if self.__funcionario_DAO.chamar(int(dados_funcionario['matricula'])):
            self.__tela_cadastrar_funcionario.pop_mensagem('Já existe um funcionário com a matrícula digitada')
        else:
            try:
                matricula = int(dados_funcionario['matricula'])
                if dados_funcionario['nome'] is not '' and dados_funcionario['matricula'] is not ' ':
                    nome = dados_funcionario['nome'].capitalize()
                if dados_funcionario['nascimento'].isdigit() and dados_funcionario['telefone'].isdigit():
                    nascimento = dados_funcionario['nascimento']
                    telefone = dados_funcionario['telefone']
                cargo = dados_funcionario['cargo']
                self.__funcionario_DAO.salvar(Funcionario(matricula, nome, nascimento, telefone, cargo))
                self.__tela_cadastrar_funcionario.pop_mensagem('Funcionário cadastrado com sucesso!')
            except:
                self.__tela_cadastrar_funcionario.pop_mensagem('Dados incorretos, funcionário não cadastrado!')
                self.abrir_tela()

    def alterar(self, funcionario):
        pass


        #if matricula in self.__funcionarios:
        #   self.__tela.imprimir('Não foi possivel cadastrar pois já existe um funcionário com essa matrícula')
        #else:
        #   self.__funcionarios[matricula] = Funcionario(matricula, nome, data_de_nascimento, telefone, cargo)
        #    self.__tela.imprimir('Funcionário cadastrado com sucesso!')

    def excluir(self, dados):
        matricula = dados[0][0].split(' ')
        print(type(matricula[0]))
        self.__funcionario_DAO.remover(int(matricula[0]))
        self.__tela_cadastrar_funcionario.pop_mensagem('Funcionário excluído com sucesso!')
        self.abrir_tela()

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