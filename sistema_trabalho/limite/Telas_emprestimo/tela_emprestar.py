from sistema_trabalho.limite.telaAbstract import TelaAbstract
import PySimpleGUI as sg


class TelaEmprestar(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}


    def configurar(self, veiculos=[]):
        layout = [
            [sg.Text('matricula'), sg.InputText(key='matricula')],
            [sg.Text('veículos cadastrados')],
            [sg.Listbox(values=veiculos, size=(65, 10), key='placa')],
            [sg.Submit('emprestar', size=(12, 2))]
        ]
        self.__janela = sg.Window('').Layout(layout)

    def abrir(self, veiculos):
        self.configurar(veiculos)
        botoes, valores = self.__janela.Read()
        return botoes, valores

    def fechar(self):
        self.__janela.Close()

