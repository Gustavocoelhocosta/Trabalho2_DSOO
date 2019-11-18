import PySimpleGUI as sg
from sistema_trabalho.limite.telaAbstract import TelaAbstract


class TelaListaFuncionario(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = dict()

    def configurar(self, funcionarios):
        layout = [
            [sg.Text('Funcionários cadastrados')],
            [sg.Listbox(values=funcionarios, size=(60, 10))],
            [sg.Button('Novo'), sg.Button('Excluir'), sg.Button('Alterar')],
            [sg.Button('Veículos permitidos'), sg.Button('Voltar')]
        ]
        self.__janela = sg.Window('Funcionários', layout)

    def abrir(self, funcionarios):
        self.configurar(funcionarios)
        self.__dados_tela = self.__janela.Read()
        botoes, valores = self.__dados_tela
        self.__janela.Close()
        return botoes, valores
