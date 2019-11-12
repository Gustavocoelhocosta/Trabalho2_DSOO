import PySimpleGUI as sg
from sistema_trabalho.limite.telaAbstract import TelaAbstract

class TelaListaVeiculo(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}

    def configurar(self, veiculos):
        layout = [
            [sg.Text('veículos cadastrados')],
            [sg.Listbox(values = veiculos, size=(60,10))],
            [sg.Submit('Novo'),sg.Submit('Excluir'), sg.Submit('Alterar'),sg.Submit('Voltar')]
             ]
        self.__janela = sg.Window('').Layout(layout)

    def abrir(self, veiculos):
        self.configurar(veiculos)
        self.__dados_tela = self.__janela.Read()
        botoes, valores = self.__dados_tela
        self.__janela.Close()
        return botoes, valores


