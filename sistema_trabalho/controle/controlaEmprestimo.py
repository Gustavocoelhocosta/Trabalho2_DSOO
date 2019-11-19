from sistema_trabalho.entidade.registro import Registro
from sistema_trabalho.limite.Telas_emprestimo.tela_emprestimo import TelaEmprestimo
from sistema_trabalho.limite.Telas_emprestimo.tela_emprestar import TelaEmprestar
from sistema_trabalho.limite.Telas_emprestimo.tela_devolver import TelaDevolver
from sistema_trabalho.limite.Telas_emprestimo.tela_registro_filtros import TelaRegistroFiltro
from sistema_trabalho.limite.Telas_emprestimo.tela_registro_lista import TelaRegistroLista
from sistema_trabalho.controle.controlaAbstract import ControlaAbstract
from sistema_trabalho.entidade.registroDAO import Registro_DAO

class ControlaEmprestimo(ControlaAbstract):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__registro_DAO = Registro_DAO()
        self.__tela_emprestimo = TelaEmprestimo()
        self.__tela_emprestar = TelaEmprestar()
        self.__tela_devolver = TelaDevolver()
        self.__tela_registro_filtro = TelaRegistroFiltro()
        self.__tela_registro_lista = TelaRegistroLista()


    @property
    def tela_emprestimo(self):
        return self.__tela_emprestimo

    @property
    def tela_emprestar(self):
        return self.__tela_emprestar

    @property
    def tela_devolver(self):
        return self.__tela_devolver

    @property
    def tela_registro_filtro(self):
        return self.__tela_registro_filtro

    @property
    def tela_registro_lista(self):
        return self.__tela_registro_lista

    def incluir(self):
        pass

    def excluir(self):
        pass


    #abre a tela inicial de emprestimo
    def abrir_tela(self):
        opcoes = {'emprestar': self.emprestar_veiculo,
                  'devolver': self.devolver_veiculo,
                  'registros': self.registros,
                  'voltar': self.voltar,
                  None: self.voltar
                  }
        botao, valores = self.__tela_emprestimo.abrir()
        opcoes[botao]()

    # empresta os veiculos
    def emprestar_veiculo(self):
        veiculos = self.__sistema.controla_veiculo.listar_veiculos()
        botoes, valores = self.__tela_emprestar.abrir(veiculos)
        if botoes == None or botoes == 'voltar':
            return self.abrir_tela()
        try:
            matricula = int(valores['m'])
        except:
            self.__tela_emprestar.pop_mensagem('matricula deve ser um inteiro')
            self.abrir_tela()
        placa = valores['p'][0][0:7]
        print(placa)
        print(matricula)
        if self.__sistema.controla_veiculo.chamar_veiculo(placa):
            veiculo = self.__sistema.controla_veiculo.chamar_veiculo(placa)
            if self.__sistema.controla_funcionario.chamar_funcionario(matricula):
                funcionario = self.__sistema.ccontrola_funcionario.chamar_funcionario(matricula)
                if veiculo.emprestado:
                    self.registrar(veiculo, funcionario, 3)
                    self.__tela_emprestar.pop_mensagem('veículo indisponível')
                if funcionario.bloqueio > 3:
                    self.registrar(veiculo, funcionario, 4)
                    self.__tela_emprestar.pop_mensagem('Acesso Bloqueado')  # raise erro
                if funcionario.cargo == 'DIRETOR' or veiculo in funcionario.veiculos.values():
                    veiculo.emprestado = True
                    self.registrar(veiculo, funcionario, 0)
                    self.__tela_emprestar.pop_mensagem('Acesso permitido ao veiculo')
                else:
                    self.registrar(veiculo, funcionario, 2)
                    funcionario.bloqueio += 1
                    self.__tela_emprestar.pop_mensagem('Não possui acesso ao veículo')
            else:
                self.registrar(veiculo, None, 1)
                self.__tela_emprestar.pop_mensagem('Matrícula não existe')  # raise erro
        else:
            self.__tela_emprestar.pop_mensagem('veiculo não existe')
        self.abrir_tela()



    #devolve o veículo mutando o status de emprestado para disponivel e atualiza a quilometragem
    def devolver_veiculo(self):
        botoes, valores = self.__tela_devolver.abrir()
        if botoes == None or botoes == 'voltar':
            return self.abrir_tela()
        try:
            veiculo = self.__sistema.controla_veiculo.chamar_veiculo(valores['pl'].upper())
            if not veiculo.emprestado:
                self.tela_emprestar.pop_mensagem('Veículo encontra-se na garagem')
                return self.abrir_tela()
            Km = int(valores[km])
            veiculo.quilometragem_atual += Km
            veiculo.emprestado = False
            self.abrir_tela()
            self.tela_emprestar.pop_mensagem('Veículo devolvido com sucesso')

        except:
            self.tela_emprestar.pop_mensagem('não foi possivel devolver o veículo, dados inconsistentes')
            return self.abrir_tela()




    #cria um registro e armazena na lista registros
    def registrar(self, veiculo, funcionario, motivo):
        registro = Registro(veiculo, funcionario, motivo)
        self.__registro_DAO.salvar(registro)
        self.tela_emprestar.pop_mensagem(registro.motivo)

    #lista os registros por filtros
    def registros(self):
        botoes, valores = self.__tela_registro_filtro.abrir()
        if botoes == None or botoes == 'voltar':
            return self.abrir_tela()
        pass


        # registros = list(self.__registro_DAO.chamar_todos())
        # filtro = botoes
        # parametro = valores
        # registros_filtrados = []
        # if filtro == 3: #lista todos os registros
        #     return self.tela_registro_lista()
        # elif filtro == 4: #voltar
        #     return None
        # else:
        #     for registro in self.__registros: #percorre todos os registros
        #         if filtro == 1: #filtra por matricula
        #             matricula = registro.funcionario.matricula
        #             if matricula == parametro:
        #                 registros_filtrados.append(registro)
        #         elif filtro == 2: #filtra por placa
        #             placa = registro.veiculo.placa
        #             if placa == parametro:
        #                 registros_filtrados.append(registro)
        #         else: #filtro por motivo
        #             motivos = ['Acesso permitido ao veiculo', 'Matrícula não existe', 'Não possui acesso ao veículo', 'veículo indisponível', 'Acesso Bloqueado']
        #             if registro.motivo == motivos[parametro]:
        #                 registros_filtrados.append(registro)
        #     self.__tela_emprestimo.listar_registros(registros_filtrados)

    def voltar(self):
        return self.__sistema.chamar_tela_inicial()