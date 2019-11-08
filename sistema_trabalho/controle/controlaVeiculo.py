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
        veiculos = self.__veiculos
        botoes, valores = self.__tela_listar_veiculo.abrir(veiculos)
        opcoes = {'Novo': self.incluir,
                  'Excluir': self.excluir,
                  'Alterar': self.alterar,
                  'Voltar': self.voltar,
                  }
        if botoes in ['Novo', 'Voltar']:
            opcoes[botoes]()
        else:
            valores = valores[0][0]
            opcoes[botoes](valores)

    def alterar(self, placa):
        veiculo = self.__veiculos[placa]
        dados_veículo = {
                        'placa': veiculo.placa,
                        'modelo': veiculo.modelo,
                        'marca': veiculo.marca,
                        'ano': veiculo.ano,
                        'km': veiculo.quilometragem_atual,
                        }
        botoes, valores = self.__tela_incluir_veiculo.abrir(dados_veículo)
        self.__veiculos[valores['placa']] = Veiculo(
                                                    valores['placa'],
                                                    valores['modelo'],
                                                    valores['marca'],
                                                    valores['ano'],
                                                    valores['quilometragem_atual']
                                                    )
        self.abrir_tela()




    def incluir(self):
        botao, dados_veiculo = self.__tela_incluir_veiculo.abrir()
        if dados_veiculo['placa'] in self.__veiculos:
            self.__tela_incluir_veiculo.pop_mensagem('veículo já cadastrado')
        else:
            try:
                placa = dados_veiculo['placa']
                modelo = dados_veiculo['modelo']
                marca = dados_veiculo['marca']
                ano = int(dados_veiculo['ano'])
                km = int(dados_veiculo['quilometragem_atual'])
                self.__veiculos[placa] = Veiculo(placa, modelo, marca, ano, km)
                self.__tela_incluir_veiculo.pop_mensagem('veiculo cadastrado com sucesso')
            except:
                self.__tela_incluir_veiculo.pop_mensagem('ano e quilometragem atual devem ser números inteiros. Veículo não cadastrado')
        self.abrir_tela()


    def excluir(self, placa):
        veiculo = self.__veiculos[placa]
        del(self.__veiculos[placa])
        self.__tela_incluir_veiculo.pop_mensagem('veiculo excluido com sucesso')
        self.abrir_tela()

        #
        # if self.buscar_veiculo_placa(placa):
        #     veiculo = self.buscar_veiculo_placa(placa)
        #     if veiculo.emprestado:
        #         self.__tela_veiculo.imprimir('veículo fora da garagem')
        #     else:
        #         del self.veiculos[placa]
        #         self.__sistema.controla_funcionario.excluir_veiculo_funcionarios(placa)
        #         self.__tela_veiculo.imprimir('veículo excluido com sucesso')
        # else:
        #     self.__tela_veiculo.imprimir('veículo inexistente')

    def listar(self):
        lista = self.__veiculos
        self.__tela_listar_veiculo.abrir(lista)

    def buscar_veiculo_placa(self, placa):
        if placa in self.__veiculos:
            return self.__veiculos[placa]
        else:
            return None

    def voltar(self):
        self.__sistema.chamar_tela_inicial()



