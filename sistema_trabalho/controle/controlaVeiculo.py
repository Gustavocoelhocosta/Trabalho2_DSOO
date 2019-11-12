from sistema_trabalho.limite.Telas_veiculo.telaVeiculo import TelaVeiculo
from sistema_trabalho.limite.Telas_veiculo.telaCadastraoVeiculo import TelaIncluirVeiculo
from sistema_trabalho.limite.Telas_veiculo.telaListaVeiculo import TelaListaVeiculo
from sistema_trabalho.entidade.veiculo import Veiculo
from sistema_trabalho.entidade.veiculoDAO import Veiculo_DAO
from sistema_trabalho.controle.controlaAbstract import ControlaAbstract
import re
from sistema_trabalho.controle.Excecoes import *


class ControlaVeiculo(ControlaAbstract):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__veiculo_DAO = Veiculo_DAO()
        self.__tela_veiculo = TelaVeiculo()
        self.__tela_incluir_veiculo = TelaIncluirVeiculo()
        self.__tela_listar_veiculo = TelaListaVeiculo()

    @property
    def veiculo_DAO(self):
        return self.__veiculo_DAO

    def abrir_tela(self):
        veiculos = []
        for veiculo in self.__veiculo_DAO.chamar_todos():
            veiculos.append(veiculo.placa + ' - ' +
                            veiculo.marca + ' - ' +
                            veiculo.modelo + ' - ' +
                            str(veiculo.ano) + ' - ' +
                            str(veiculo.quilometragem_atual))
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
        placa = placa[0:7]
        veiculo = self.veiculo_DAO.chamar(placa)
        dados_veiculo = {
                        'placa': veiculo.placa,
                        'modelo': veiculo.modelo,
                        'marca': veiculo.marca,
                        'ano': veiculo.ano,
                        'km': veiculo.quilometragem_atual,
                        }
        botoes, valores = self.__tela_incluir_veiculo.abrir(dados_veiculo)
        if placa != valores['placa']:
            self.__veiculo_DAO.remover(placa)
        veiculo_alterado = Veiculo(valores['placa'],
                          valores['modelo'],
                          valores['marca'],
                          valores['ano'],
                          valores['quilometragem_atual']
                          )
        self.__veiculo_DAO.salvar(veiculo_alterado)
        self.abrir_tela()




    def incluir(self):
        botao, dados_veiculo = self.__tela_incluir_veiculo.abrir()
        if self.veiculo_DAO.chamar(dados_veiculo['placa']):
            self.__tela_incluir_veiculo.pop_mensagem('veículo já cadastrado')
        else:
            try:
                placa = dados_veiculo['placa']
                modelo = dados_veiculo['modelo']
                marca = dados_veiculo['marca']
                ano = int(dados_veiculo['ano'])
                km = int(dados_veiculo['quilometragem_atual'])
                veiculo = Veiculo(placa, modelo, marca, ano, km)
                self.__veiculo_DAO.salvar(veiculo)
                self.__tela_incluir_veiculo.pop_mensagem('veiculo cadastrado com sucesso')
            except:
                self.__tela_incluir_veiculo.pop_mensagem('ano e quilometragem atual devem ser números inteiros. Veículo não cadastrado')
        self.abrir_tela()


    def excluir(self, placa):
        placa = placa[0:7]
        self.__veiculo_DAO.remover(placa)
        self.__tela_incluir_veiculo.pop_mensagem('veiculo excluido com sucesso')
        self.abrir_tela()

    def voltar(self):
        self.__sistema.chamar_tela_inicial()



