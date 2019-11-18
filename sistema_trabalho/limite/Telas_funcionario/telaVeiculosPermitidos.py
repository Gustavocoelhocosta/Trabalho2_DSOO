import PySimpleGUI as sg
from sistema_trabalho.limite.telaAbstract import TelaAbstract

class TelaVeiculosPermitidos(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = dict()

    def configurar(self, veiculos = []):
        layout = [
            [sg.Text('Vecículos permitidos')],
            [sg.Listbox(values=list(veiculos), size=(60, 10))],
            [sg.Button('Novo'), sg.Button('Excluir'), sg.Button('Voltar')]
        ]
        self.__janela = sg.Window('Veículos permitidos', layout)

    def abrir(self, veiculos):
        self.configurar(veiculos)
        self.__dados_tela = self.__janela.Read()
        botoes, valores = self.__dados_tela
        self.__janela.Close()
        return botoes, valores