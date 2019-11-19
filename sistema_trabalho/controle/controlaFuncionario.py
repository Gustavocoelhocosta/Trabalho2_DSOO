from sistema_trabalho.limite.Telas_funcionario.telaCadastraFuncionario import TelaIncluirFuncionario
from sistema_trabalho.limite.Telas_funcionario.telaListaFuncionario import TelaListaFuncionario
from sistema_trabalho.limite.Telas_funcionario.telaVeiculosPermitidos import TelaVeiculosPermitidos
from sistema_trabalho.limite.Telas_funcionario.telaCadastraVeiculoNoFuncionario import TelaCadastraVeiculoNoFuncionario
from sistema_trabalho.entidade.funcionario import Funcionario
from sistema_trabalho.entidade.funcionarioDAO import FuncionarioDAO
from sistema_trabalho.controle.controlaAbstract import ControlaAbstract

class ControlaFuncionario(ControlaAbstract):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__funcionario_DAO = FuncionarioDAO()
        self.__tela_listar_funcionarios = TelaListaFuncionario()
        self.__tela_cadastrar_funcionario = TelaIncluirFuncionario()
        self.__tela_veiculos_permitidos = TelaVeiculosPermitidos()
        self.__tela_cadastrar_veiculo_no_funcionario = TelaCadastraVeiculoNoFuncionario()
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
        print(botoes, len(valores[0]))
        opcoes = {'Novo': self.incluir,
                  'Excluir': self.excluir,
                  'Alterar': self.alterar,
                  'Veículos permitidos': self.veiculos_funcionario,
                  'Voltar': self.voltar,
                  None: self.voltar}
        if botoes in ['Alterar', 'Excluir', 'Veículos permitidos']:
            try:
                opcoes[botoes](valores)
                self.abrir_tela()
            except:
                self.abrir_tela()
        else:
            opcoes[botoes]()
            self.abrir_tela()

    def incluir(self):
        botoes, dados_funcionario = self.__tela_cadastrar_funcionario.abrir(None, self.__cargos)
        if dados_funcionario['matricula'] == '' or not dados_funcionario['matricula'].isdigit():
            self.__tela_cadastrar_funcionario.pop_mensagem('Dados incorretos, funcionário não cadastrado!')
            self.abrir_tela()
        elif self.__funcionario_DAO.chamar(int(dados_funcionario['matricula'])):
            self.__tela_cadastrar_funcionario.pop_mensagem('Já existe um funcionário com a matrícula digitada')
        else:
            try:
                matricula = int(dados_funcionario['matricula'])
                if dados_funcionario['nome'] is not '' and dados_funcionario['matricula'] is not ' ':
                    nome = dados_funcionario['nome'].capitalize()
                if dados_funcionario['nascimento'].isdigit() and dados_funcionario['telefone'].isdigit():
                    nascimento = dados_funcionario['nascimento']
                    telefone = dados_funcionario['telefone']
                if dados_funcionario['cargo'] in self.__cargos:
                    cargo = dados_funcionario['cargo']
                self.__funcionario_DAO.salvar(Funcionario(matricula, nome, nascimento, telefone, cargo))
                self.__tela_cadastrar_funcionario.pop_mensagem('Funcionário cadastrado com sucesso!')
            except:
                self.__tela_cadastrar_funcionario.pop_mensagem('Dados incorretos, funcionário não cadastrado!')
                self.abrir_tela()

    def alterar(self, dados):
        matricula = self.retorna_matricula(dados)
        funcionario = self.__funcionario_DAO.chamar(matricula)
        veiculos_permitidos = funcionario.veiculos
        dados = {'matricula': funcionario.matricula,
                 'nome': funcionario.nome,
                 'nascimento': funcionario.data_de_nascimento,
                 'telefone': funcionario.telefone,
                 'cargo': funcionario.cargo
                 }
        botoes, valores = self.__tela_cadastrar_funcionario.abrir(dados, self.__cargos)

        if botoes == 'Incluir':
            try:
                matricula_alterada = int(valores['matricula'])
                if valores['nome'] is not '' and valores['matricula'] is not ' ':
                    nome = valores['nome'].capitalize()
                if valores['nascimento'].isdigit() and valores['telefone'].isdigit():
                    nascimento = valores['nascimento']
                    telefone = valores['telefone']
                if valores['cargo'] in self.__cargos:
                    cargo = valores['cargo']
                self.__funcionario_DAO.remover(matricula)
                self.__funcionario_DAO.salvar(Funcionario(matricula_alterada, nome, nascimento, telefone, cargo))
                funcionario_alterado = self.__funcionario_DAO.chamar(matricula_alterada)
                funcionario_alterado.veiculos = veiculos_permitidos
                self.__funcionario_DAO.salvar(funcionario_alterado)
                self.__tela_cadastrar_funcionario.pop_mensagem('Funcionário alterado com sucesso!')
            except:
                self.__tela_cadastrar_funcionario.pop_mensagem('Dados incorretos, funcionário não alterado!')
                self.abrir_tela()


    def excluir(self, dados):
        self.__funcionario_DAO.remover(self.retorna_matricula(dados))
        self.__tela_cadastrar_funcionario.pop_mensagem('Funcionário excluído com sucesso!')
        self.abrir_tela()

    def listar(self):
        self.__funcionario_DAO.chamar_todos()

    def veiculos_funcionario(self, dados):
        funcionario = self.__funcionario_DAO.chamar(self.retorna_matricula(dados))
        botoes, valores = self.__tela_veiculos_permitidos.abrir(funcionario.veiculos)
        print(botoes, valores)
        opcoes = {'Novo': self.cadastrar_veiculo_no_funcionario,
                  'Excluir': self.excluir_veiculo_do_funcionario,
                  'Voltar': self.abrir_tela}
        if botoes == 'Novo':
            opcoes[botoes](funcionario.matricula)
            self.abrir_tela()
        elif botoes == 'Excluir':
            opcoes[botoes](funcionario.matricula, valores)
        else:
            opcoes[botoes]()
            self.abrir_tela()

    def cadastrar_veiculo_no_funcionario(self, matricula):
        botoes, valores = self.__tela_cadastrar_veiculo_no_funcionario.abrir(self.__sistema.controla_veiculo.listar_veiculos())
        if botoes == 'Cadastrar':
            placa = valores[0][0].split(' - ')[0]
            funcionario = self.__funcionario_DAO.chamar(matricula)
            veiculo = self.__sistema.controla_veiculo.chamar_veiculo(placa)
            funcionario.veiculos[placa] = veiculo
            self.__funcionario_DAO.salvar(funcionario)


    def excluir_veiculo_do_funcionario(self, matricula, valores):
        funcionario = self.__funcionario_DAO.chamar(matricula)
        placa = valores[0][0]
        del(funcionario.veiculos[placa])
        self.__funcionario_DAO.salvar(funcionario)
        self.abrir_tela()


    def listar_veiculos_permitidos(self, matricula):
        return self.__funcionario_DAO.chamar(matricula).veiculos


    #preciso dessa função que busque o funcionario na DAO, retorna Funcionario
    def chamar_funcionario(self, matricula):
        return self.__funcionario_DAO.chamar(matricula)
    #----------------------------------------------------------

    def voltar(self):
        self.__sistema.chamar_tela_inicial()

    def retorna_matricula(self, dados):
        lista_dados = dados[0][0].split('-')
        return int(lista_dados[0])
