from abc import ABC, abstractclassmethod
# from sistema_trabalho.controle.Excecoes import *
import re
import PySimpleGUI as sg


class TelaAbstract(ABC):

    def fechar(self):
        pass


    def confirmar_saida(self):
        sg.Popup('Title',
                 'Finalizar o programa.',
                 sg.Submit('Sim', key=2),
                 sg.Submit('Não', key=2))


    def pop_mensagem(self,mensagem):
        sg.Popup(mensagem)
    #----------------------------------------------------------------------------------

    def imprimir(self, conteudo):
        print(conteudo)

    def listar_veiculos(self, lista):
        print('PLACA - MODELO - MARCA - ANO - QUILOMETRAGEM')
        for veiculo in lista:
            print('%s - %s - %s - %d - %d'% (lista[veiculo].placa, lista[veiculo].modelo, lista[veiculo].marca, lista[veiculo].ano, lista[veiculo].quilometragem_atual))

    def pedir_inteiro_valido(self, mensagem = 'digite um inteiro válido', validos = [], mensagem_erro = 'não é um inteiro válido'):
        while True:
            inteiro = input(mensagem)
            try:
                inteiro = int(inteiro)
                if not validos:
                    return inteiro
                elif inteiro in validos:
                    return inteiro
                else:
                    raise InteiroInvalido()
            except: InteiroInvalido()
            print(mensagem_erro)

    def pedir_placa(self):
        while True:
            try:
                pafrao_placa = re.compile('^[A-Z]{3}\d{4}$')
                placa = input('digite a placa - ').upper()
                if re.match(pafrao_placa, placa):
                    return placa
                else:
                    raise PlacaInvalida()
            except: PlacaInvalida()
            print('digite três letras seguidas de 3 números Ex: (AAA0000) ')

    def pedir_matricula(self):
        return self.pedir_inteiro_valido('Digite a matrícula: ')


