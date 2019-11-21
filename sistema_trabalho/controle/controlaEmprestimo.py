from sistema_trabalho.entidade.registro import Registro
from sistema_trabalho.limite.Telas_emprestimo.tela_emprestimo import TelaEmprestimo
from sistema_trabalho.limite.Telas_emprestimo.tela_emprestar import TelaEmprestar
from sistema_trabalho.limite.Telas_emprestimo.tela_devolver import TelaDevolver
from sistema_trabalho.limite.Telas_emprestimo.tela_registro_filtros import TelaRegistroFiltro
from sistema_trabalho.limite.Telas_emprestimo.tela_registro_lista import TelaRegistroLista
from sistema_trabalho.controle.controlaAbstract import ControlaAbstract
from sistema_trabalho.percistencia.registroDAO import Registro_DAO

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
            return self.abrir_tela()

        placa = valores['p'][0][0:7]
        if self.__sistema.controla_veiculo.chamar_veiculo(placa):
            veiculo = self.__sistema.controla_veiculo.chamar_veiculo(placa)
            if self.__sistema.controla_funcionario.chamar_funcionario(matricula):
                funcionario = self.__sistema.controla_funcionario.chamar_funcionario(matricula)
                if veiculo.emprestado:
                    self.registrar(veiculo, funcionario, 3)
                    self.__tela_emprestar.pop_mensagem('veículo indisponível')
                elif funcionario.bloqueio > 3:
                    self.registrar(veiculo, funcionario, 4)
                    self.__tela_emprestar.pop_mensagem('Acesso Bloqueado')
                elif funcionario.cargo == 'Direção' or veiculo in funcionario.veiculos.values():
                    veiculo.emprestado = True
                    self.__sistema.controla_veiculo.veiculo_DAO.salvar(veiculo)
                    self.registrar(veiculo, funcionario, 0)
                    self.__tela_emprestar.pop_mensagem('Acesso permitido ao veiculo')
                else:
                    self.registrar(veiculo, funcionario, 2)
                    funcionario.bloqueio += 1
                    self.__sistema.controla_funcionario.funcionarios_DAO.salvar(funcionario)
                    self.__tela_emprestar.pop_mensagem('Não possui acesso ao veículo')
            else:
                self.registrar(veiculo, None, 1)
                self.__tela_emprestar.pop_mensagem('Matrícula não existe')
        else:
            return self.__tela_emprestar.pop_mensagem('veiculo não existe')
        return self.abrir_tela()


    #devolve o veículo mutando o status de emprestado para disponivel e atualiza a quilometragem
    def devolver_veiculo(self):
        placas = self.__sistema.controla_veiculo.listar_placas()
        botoes, valores = self.__tela_devolver.abrir(placas)
        if botoes == None or botoes == 'voltar':
            return self.abrir_tela()

        if self.__sistema.controla_veiculo.chamar_veiculo(valores['pl'].upper()):
            veiculo = self.__sistema.controla_veiculo.chamar_veiculo(valores['pl'].upper())
            if not veiculo.emprestado:
                self.tela_emprestar.pop_mensagem('não foi possivel devolver o veículo, veículo encontra-se na garagem')
                return self.devolver_veiculo()
            try:
                Km = int(valores['km'])
            except:
                self.tela_emprestar.pop_mensagem('Quilometragem deve ser um inteiro')
                return self.devolver_veiculo()
        else:
            self.tela_emprestar.pop_mensagem('não foi possivel devolver o veículo, dados inconsistentes')
            return self.devolver_veiculo()
        veiculo.quilometragem_atual += Km
        veiculo.emprestado = False
        self.__sistema.controla_veiculo.veiculo_DAO.salvar(veiculo)
        self.tela_emprestar.pop_mensagem('Veículo devolvido com sucesso')
        return self.abrir_tela()





    #cria um registro e armazena na lista registros
    def registrar(self, veiculo, funcionario, motivo):
        registro = Registro(veiculo, funcionario, motivo)
        self.__registro_DAO.salvar(registro)


    #lista os registros por filtros
    def registros(self):
        placas = self.__sistema.controla_veiculo.listar_placas()
        matriculas = self.__sistema.controla_funcionario.listar_matriculas()
        botoes, valores = self.__tela_registro_filtro.abrir(placas, matriculas)
        if botoes == None or botoes == 'voltar':
            return self.abrir_tela()
        else:
            registros_filtrados = []
            if botoes == 'Todos':
                for registro in self.__registro_DAO.chamar_todos():
                    registros_filtrados.append(self.formatar_registro(registro))
            elif botoes == 'por plcaca':
                for registro in self.__registro_DAO.chamar_todos():
                    if registro.veiculo.placa == valores['pl']:
                        registros_filtrados.append(self.formatar_registro(registro))
            elif botoes == 'por motivo':
                for registro in self.__registro_DAO.chamar_todos():
                    if registro.motivo == valores['motivo']:
                        registros_filtrados.append(self.formatar_registro(registro))
            elif botoes == 'por matrícula':
                for registro in self.__registro_DAO.chamar_todos():
                    if registro.funcionario:
                        if registro.funcionario.matricula == valores['matricula']:
                            registros_filtrados.append(self.formatar_registro(registro))
            self.__tela_registro_lista.abrir(registros_filtrados)
            return self.registros()

    def formatar_registro(self, registro):
        if registro.funcionario:
            funcionario = str(registro.funcionario.matricula)
        else:
            funcionario = 'None'
        veiculo = registro.veiculo.placa
        motivo = registro.motivo
        data = str(registro.data_hora)
        return veiculo + ' - ' + funcionario + ' - ' + motivo + ' - ' + data

    def voltar(self):
        return self.__sistema.chamar_tela_inicial()