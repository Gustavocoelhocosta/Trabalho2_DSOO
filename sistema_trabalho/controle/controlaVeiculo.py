from sistema_trabalho.limite.Telas_veiculo.telaCadastraoVeiculo import TelaIncluirVeiculo
from sistema_trabalho.limite.Telas_veiculo.telaListaVeiculo import TelaListaVeiculo
from sistema_trabalho.entidade.veiculo import Veiculo
from sistema_trabalho.entidade.veiculoDAO import Veiculo_DAO
from sistema_trabalho.controle.controlaAbstract import ControlaAbstract
import re
# from sistema_trabalho.controle.Excecoes import *


class ControlaVeiculo(ControlaAbstract):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__veiculo_DAO = Veiculo_DAO()
        self.__tela_incluir_veiculo = TelaIncluirVeiculo()
        self.__tela_listar_veiculo = TelaListaVeiculo()

    @property
    def veiculo_DAO(self):
        return self.__veiculo_DAO

    def abrir_tela(self):
        veiculos = self.listar_veiculos()
        botoes, valores = self.__tela_listar_veiculo.abrir(veiculos)
        opcoes = {'Novo': self.incluir,
                  'Excluir': self.excluir,
                  'Alterar': self.alterar,
                  'Voltar': self.voltar,
                  None : self.voltar
                  }
        if botoes in ['Novo', 'Voltar', None]:
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
        dados_veiculo_alterado = valores
        try:
            placa = self.valida_placa(dados_veiculo_alterado['placa'].upper())
            modelo = dados_veiculo_alterado['modelo'].upper()
            marca = dados_veiculo_alterado['marca'].upper()
            ano = int(dados_veiculo_alterado['ano'])
            km = int(dados_veiculo_alterado['quilometragem_atual'])
            if not (placa and modelo and marca and ano and km):
                raise Exception
            if placa != valores['placa']:
                self.__veiculo_DAO.remover(placa)
            veiculo_alterado = Veiculo(placa, modelo, marca, ano, km)
            self.__veiculo_DAO.salvar(veiculo_alterado)
            self.abrir_tela()
        except Exception:
            self.__tela_incluir_veiculo.pop_mensagem('Veículo não cadastrado, dados incompletos ou incompativeis')
            self.abrir_tela()


    def incluir(self):
        botao, dados_veiculo = self.__tela_incluir_veiculo.abrir()
        if self.veiculo_DAO.chamar(dados_veiculo['placa'].upper()):
            self.__tela_incluir_veiculo.pop_mensagem('veículo já cadastrado')
        else:
            try:
                placa = self.valida_placa(dados_veiculo['placa'].upper())
                modelo = dados_veiculo['modelo'].upper()
                marca = dados_veiculo['marca'].upper()
                ano = int(dados_veiculo['ano'])
                km = int(dados_veiculo['quilometragem_atual'])
                if not(placa and modelo and marca and ano and km):
                    raise Exception
                veiculo = Veiculo(placa, modelo, marca, ano, km)
                self.__veiculo_DAO.salvar(veiculo)
                self.__tela_incluir_veiculo.pop_mensagem('veiculo cadastrado com sucesso')
            except Exception:
                self.__tela_incluir_veiculo.pop_mensagem('Veículo não cadastrado, dados incompletos ou incompativeis')
        self.abrir_tela()


    def excluir(self, placa):
        placa = placa[0:7]
        self.__veiculo_DAO.remover(placa)
        self.__tela_incluir_veiculo.pop_mensagem('veiculo excluido com sucesso')
        self.abrir_tela()

    def valida_placa(self, placa):
        pafrao_placa = re.compile('^[A-Z]{3}\d{4}$')
        if re.match(pafrao_placa, placa):
            return placa
        else:
            return None

    def chamar_veiculo(self, placa):
        return self.__veiculo_DAO.chamar(placa)

    def listar_veiculos(self):
        veiculos = []
        for veiculo in self.__veiculo_DAO.chamar_todos():
            if veiculo.emprestado:
                emprestado = 'INDISPONÍVEL'
            else:
                emprestado = 'DISPONÍVEL'
            veiculos.append(str(veiculo.placa) + ' - '  + emprestado  + ' - ' + str(veiculo.modelo) + ' - ' + str(veiculo.marca) + ' - ' + str(veiculo.ano) + ' - ' + str(veiculo.quilometragem_atual))
        return veiculos

    def listar_placas(self):
        placas = []
        for veiculo in self.__veiculo_DAO.chamar_todos():
            placas.append(veiculo.placa)
        return placas

    def voltar(self):
        return self.__sistema.chamar_tela_inicial()
