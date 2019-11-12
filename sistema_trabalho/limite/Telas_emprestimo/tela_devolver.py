from sistema_trabalho.limite.telaAbstract import TelaAbstract
import PySimpleGUI as sg


class TelaDevolver(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}
        self.configurar()

    def configurar(self, lista=[]):
        layout = [
            [sg.Text('placa', size=(17,1)), sg.InputText()],
            [sg.Text('quilometragem rodada', size=(17,1)), sg.InputText()],
            [sg.Submit('devolver', size=(12, 2))]
        ]
        self.__janela = sg.Window('').Layout(layout)

    def abrir(self):
        botoes, valores = self.__janela.Read()
        return botoes, valores

    def fechar(self):
        self.__janela.Close()

