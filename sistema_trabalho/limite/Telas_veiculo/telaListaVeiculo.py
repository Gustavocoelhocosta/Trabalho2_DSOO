import PySimpleGUI as sg
from sistema_trabalho.limite.telaAbstract import TelaAbstract

class TelaListaVeiculo(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}

    def configurar(self, veiculos):
        layout = [
            [sg.Text('veículos cadastrados')],
            [sg.Listbox(values = veiculos, size=(65,10))],
            [sg.Submit('Novo',size=(12,2)),sg.Submit('Excluir',size=(12,2)), sg.Submit('Alterar',size=(12,2)),sg.Submit('Voltar',size=(10,2))]
             ]
        self.__janela = sg.Window('Veículos').Layout(layout)

    def abrir(self, veiculos):
        self.configurar(veiculos)
        self.__dados_tela = self.__janela.Read()
        botoes, valores = self.__dados_tela
        self.__janela.Close()
        return botoes, valores


