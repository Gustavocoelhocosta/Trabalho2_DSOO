from sistema_trabalho.limite.telaVeiculo import *
from sistema_trabalho.entidade.veiculo import Veiculo
from sistema_trabalho.controle.controlaAbstract import ControlaAbstract
from sistema_trabalho.controle.Excecoes import *


class ControlaVeiculo(ControlaAbstract):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__veiculos = {}
        self.__tela_veiculo = TelaVeiculo()
        self.__tela_incluir_veiculo = TelaIncluirVeiculo()

    @property
    def veiculos(self):
        return self.__veiculos

    def abrir_tela(self):
        opcoes = {0: self.incluir, 1: self.excluir, 3: self.listar, 2: self.alterar, 4: self.voltar, None: self.voltar}
        botao = self.__tela_veiculo.abrir()
        opcoes[botao]()
        self.abrir_tela()


    def incluir(self):
        try:
            dados_veiculo = self.__tela_incluir_veiculo.incluir_veiculo()
            placa = dados_veiculo[0]
            modelo = dados_veiculo[1]
            marca = dados_veiculo[2]
            ano = int(dados_veiculo[3])
            quilometragem_atual = int(dados_veiculo[4])
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

    def alterar(self):
        pass

    def voltar(self):
        self.__sistema.chamar_tela_inicial()



