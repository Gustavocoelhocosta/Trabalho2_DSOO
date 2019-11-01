from sistema_trabalho.entidade.registro import Registro
from sistema_trabalho.limite.telaEmprestimo import TelaEmprestimo
from sistema_trabalho.controle.controlaAbstract import ControlaAbstract
#

class ControlaEmprestimo(ControlaAbstract):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__registros = []
        self.__tela_emprestimo = TelaEmprestimo()

    @property
    def registros(self):
        return self.__registros

    @property
    def tela_emprestimo(self):
        return self.__tela_emprestimo

    def incluir(self):
        pass

    def excluir(self):
        pass


    #abre a tela inicial de emprestimo
    def abrir_tela(self):
        self.__tela_emprestimo.imprimir('----------------------------------------------------')
        opcoes = {0: self.emprestar_veiculo, 1: self.devolver_veiculo, 2: self.listar, 3: self.voltar}
        opcao = self.__tela_emprestimo.listar_opcoes()
        opcoes[opcao]()
        return self.abrir_tela()

    #empresta os veiculos
    def emprestar_veiculo(self):
        self.__sistema.controla_funcionario.listar()
        matricula = self.__tela_emprestimo.pedir_matricula()
        self.__sistema.controla_veiculo.listar()
        placa = self.__tela_emprestimo.pedir_placa()
        tela = self.__tela_emprestimo
        if self.__sistema.controla_veiculo.buscar_veiculo_placa(placa):
            veiculo = self.__sistema.controla_veiculo.buscar_veiculo_placa(placa)
        else:
            tela.imprimir('veiculo inexistente')
            return self.emprestar_veiculo()
        if self.__sistema.controla_funcionario.buscar_funcionario_matricula(matricula):
            funcionario = self.__sistema.controla_funcionario.buscar_funcionario_matricula(matricula)
            if funcionario.bloqueio >= 3:
                return self.registrar(veiculo, funcionario, 4) #Acesso Bloqueado
            if not veiculo.emprestado:
                if funcionario.cargo == "DIRETOR" or funcionario.cargo == "DIRETORA" or placa in funcionario.veiculos:
                    veiculo.emprestado = True
                    return self.registrar(veiculo, funcionario, 0) #Acesso permitido ao veiculo
                else:
                    funcionario.bloqueio += 1
                    return self.registrar(veiculo, funcionario, 2)  #Não possui acesso ao veículo
            else:
                return self.registrar(veiculo, funcionario, 3) #veículo indisponível
        else:
            return self.registrar(veiculo, None, 1) # Matrícula não existe


    #devolve o veículo mutando o status de emprestado para disponivel e atualiza a quilometragem
    def devolver_veiculo(self):
        dados = self.__tela_emprestimo.devolver_veiculo()
        placa = dados[0]
        quilometros_rodados = dados[1]
        veiculo = self.__sistema.controla_veiculo.veiculos[placa]
        veiculo.quilometragem_atual += quilometros_rodados
        veiculo.emprestado = False
        self.abrir_tela()

    #cria um registro e armazena na lista registros
    def registrar(self, veiculo, funcionario, motivo):
        registro = Registro(veiculo, funcionario, motivo)
        self.__registros.append(registro)
        self.__tela_emprestimo.imprimir(registro.motivo)

    #lista os registros por filtros
    def listar(self):
        dados = self.__tela_emprestimo.listar_filtro_registro()
        filtro = dados[0]
        parametro = dados[1]
        registros_filtrados = []
        if filtro == 3: #lista todos os registros
            return self.__tela_emprestimo.listar_registros(self.__registros)
        elif filtro == 4: #voltar
            return None
        else:
            for registro in self.__registros: #percorre todos os registros
                if filtro == 1: #filtra por matricula
                    matricula = registro.funcionario.matricula
                    if matricula == parametro:
                        registros_filtrados.append(registro)
                elif filtro == 2: #filtra por placa
                    placa = registro.veiculo.placa
                    if placa == parametro:
                        registros_filtrados.append(registro)
                else: #filtro por motivo
                    motivos = ['Acesso permitido ao veiculo', 'Matrícula não existe', 'Não possui acesso ao veículo', 'veículo indisponível', 'Acesso Bloqueado']
                    if registro.motivo == motivos[parametro]:
                        registros_filtrados.append(registro)
            self.__tela_emprestimo.listar_registros(registros_filtrados)

    def voltar(self):
        self.__sistema.chamar_tela_inicial()

    def validar_veiculo(self, placa):
        if placa in self.__sistema.controla_veiculo.veiculos:
            return placa
        else:
            print('Veículo não cadastrado')
            return self.validar_veiculo(self.__tela_emprestimo.pedir_placa())