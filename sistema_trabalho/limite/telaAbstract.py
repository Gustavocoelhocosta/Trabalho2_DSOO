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


