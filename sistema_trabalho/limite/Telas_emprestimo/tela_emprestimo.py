from sistema_trabalho.limite.telaAbstract import TelaAbstract
import PySimpleGUI as sg


class TelaEmprestimo(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}


    def configurar(self):
        layout = [
            [sg.Button('emprestar',size=(30,3))],
            [sg.Button('devolver',size=(30,3))],
            [sg.Button('registros',size=(30,3))],
            [sg.Button('voltar',size=(30,3))],
        ]
        self.__janela = sg.Window('').Layout(layout)

    def abrir(self):
        self.configurar()
        self.__dados_tela = self.__janela.Read()
        botoes, valores = self.__dados_tela
        self.__janela.Close()
        return botoes, valores

    def fechar(self):
        self.__janela.Close()
