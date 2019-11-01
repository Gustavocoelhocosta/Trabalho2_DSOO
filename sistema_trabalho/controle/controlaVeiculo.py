from sistema_trabalho.limite.telaVeiculo import TelaVeiculo
from sistema_trabalho.entidade.veiculo import Veiculo
from sistema_trabalho.controle.controlaAbstract import ControlaAbstract
from sistema_trabalho.controle.Excecoes import *


class ControlaVeiculo(ControlaAbstract):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__veiculos = {}
        self.__tela_veiculo = TelaVeiculo()

    @property
    def veiculos(self):
        return self.__veiculos

    def abrir_tela(self):
        self.__tela_veiculo.imprimir('----------------------------------------------------')
        opcoes = {0: self.incluir, 1: self.excluir, 2: self.listar, 3: self.voltar}
        opcao = self.__tela_veiculo.listar_opcoes()
        opcoes[opcao]()

        return self.abrir_tela()

    def incluir(self):
        try:
            self.__tela_veiculo.imprimir('cadastro de novo veiculo')
            dados_veiculo = self.__tela_veiculo.pedir_dados_veiculo()
            placa = dados_veiculo[0]
            modelo = dados_veiculo[1]
            marca = dados_veiculo[2]
            ano = dados_veiculo[3]
            quilometragem_atual = dados_veiculo[4]
            if self.buscar_veiculo_placa(placa):
                raise VeiculoJaCadastrado()
            else:
                self.__veiculos[placa] = Veiculo(placa, modelo, marca, ano, quilometragem_atual)
                return self.__tela_veiculo.imprimir('veiculo cadastrado com sucesso')
        except: VeiculoJaCadastrado()
        self.__tela_veiculo.imprimir('não foi possível incluir, veículo já cadastrado')

    def excluir(self):
        self.listar()
        placa = self.__tela_veiculo.pedir_placa()
        if self.buscar_veiculo_placa(placa):
            veiculo = self.buscar_veiculo_placa(placa)
            if veiculo.emprestado:
                self.__tela_veiculo.imprimir('veículo fora da garagem')
            else:
                del self.veiculos[placa]
                self.__sistema.controla_funcionario.excluir_veiculo_funcionarios(placa)
                self.__tela_veiculo.imprimir('veículo excluido com sucesso')
        else:
            self.__tela_veiculo.imprimir('veículo inexistente')

    def listar(self):
        lista = self.__veiculos
        self.__tela_veiculo.listar_veiculos(lista)

    def buscar_veiculo_placa(self, placa):
        if placa in self.__veiculos:
            return self.__veiculos[placa]
        else:
            return None

    def voltar(self):
        self.__sistema.chamar_tela_inicial()



