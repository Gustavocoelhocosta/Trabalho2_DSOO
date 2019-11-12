from sistema_trabalho.limite.telaAbstract import TelaAbstract
import PySimpleGUI as sg


class TelaEmprestimo(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}
        self.configurar()

    def configurar(self):
        layout = [
            [sg.Submit('emprestar', key=0,size=(30,3))],
            [sg.Submit('devolver', key=1,size=(30,3))],
            [sg.Submit('registros', key=2,size=(30,3))],
            [sg.Submit('voltar', key=3,size=(30,3))],
        ]
        self.__janela = sg.Window('').Layout(layout)

    def abrir(self):
        botoes, valores = self.__janela.Read()
        return botoes, valores

    def fechar(self):
        self.__janela.Close()

