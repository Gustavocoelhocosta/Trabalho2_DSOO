import PySimpleGUI as sg
from sistema_trabalho.limite.telaAbstract import TelaAbstract

class TelaListaVeiculo(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}

    def configurar(self, veiculos):
        layout = [
            [sg.Listbox(values = list(veiculos), size=(30,3))],
            [sg.Submit('Novo'),sg.Submit('Excluir'), sg.Submit('Alterar'),sg.Submit('Voltar')]
             ]
        self.__janela = sg.Window('').Layout(layout)

    def abrir(self, veiculos):
        self.configurar(veiculos)
        self.__dados_tela = self.__janela.Read()
        botoes, valores = self.__dados_tela
        print(botoes)
        self.__janela.Close()
        return botoes, valores


