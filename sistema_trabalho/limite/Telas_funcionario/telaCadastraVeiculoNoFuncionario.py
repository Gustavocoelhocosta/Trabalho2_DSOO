import PySimpleGUI as sg
from sistema_trabalho.limite.telaAbstract import TelaAbstract

class TelaCadastraVeiculoNoFuncionario(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = dict()

    def configurar(self, veiculos):
        layout = [
            [sg.Text('Cadastrar veículo para o funcionário')],
            [sg.Listbox(values=list(veiculos), size=(60, 10))],
            [sg.Button('Cadastrar'), sg.Button('Voltar')]
        ]
        self.__janela = sg.Window('Cadastrar veículo para o funcionário', layout)

    def abrir(self, veiculos):
        self.configurar(veiculos)
        self.__dados_tela = self.__janela.Read()
        botoes, valores = self.__dados_tela
        self.__janela.Close()
        return botoes, valores