from sistema_trabalho.limite.Telas_veiculo.telaVeiculo import TelaVeiculo
from sistema_trabalho.limite.Telas_veiculo.telaCadastraoVeiculo import TelaIncluirVeiculo
from sistema_trabalho.limite.Telas_veiculo.telaListaVeiculo import TelaListaVeiculo
from sistema_trabalho.entidade.veiculo import Veiculo
from sistema_trabalho.controle.controlaAbstract import ControlaAbstract
from sistema_trabalho.controle.Excecoes import *


class ControlaVeiculo(ControlaAbstract):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__veiculos = {}
        self.__tela_veiculo = TelaVeiculo()
        self.__tela_incluir_veiculo = TelaIncluirVeiculo()
        self.__tela_listar_veiculo = TelaListaVeiculo()

    @property
    def veiculos(self):
        return self.__veiculos

    def abrir_tela(self):
        botoes, valores = self.__tela_listar_veiculo.abrir(self.__veiculos)
        opcoes = {'Novo': self.incluir,
                  'Excluir': self.excluir,
                  'Alterar': self.alterar,
                  'Voltar': self.voltar,
                  }
        opcoes[botoes]()
        self.abrir_tela()



    def incluir(self):
        # try:
        botao, dados_veiculo = self.__tela_incluir_veiculo.abrir()
        print(botao)
        print(dados_veiculo)
        self.__veiculos[dados_veiculo['placa']] = Veiculo(
                                         dados_veiculo['placa'],
                                         dados_veiculo['modelo'],
                                         dados_veiculo['marca'],
                                         dados_veiculo['ano'],
                                         dados_veiculo['quilometragem_atual']
                                         )
        self.__tela_incluir_veiculo.pop_mensagem('veiculo cadastrado com sucesso')

        #     if self.buscar_veiculo_placa(placa):
        #         raise VeiculoJaCadastrado()
        #     else:
        #         self.__veiculos[placa] = Veiculo(placa, modelo, marca, ano, quilometragem_atual)
        #         return self.__tela_veiculo.imprimir('veiculo cadastrado com sucesso')
        # except: VeiculoJaCadastrado()
        # self.__tela_veiculo.imprimir('não foi possível incluir, veículo já cadastrado')

    def excluir(self, placa):
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
        self.__tela_listar_veiculo.abrir(lista)

    def buscar_veiculo_placa(self, placa):
        if placa in self.__veiculos:
            return self.__veiculos[placa]
        else:
            return None

    def alterar(self):
        pass

    def voltar(self):
        self.__sistema.chamar_tela_inicial()



