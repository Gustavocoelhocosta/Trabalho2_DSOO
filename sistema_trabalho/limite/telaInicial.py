from sistema_trabalho.limite.telaAbstract import TelaAbstract
import PySimpleGUI as sg


class TelaInicial(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}
        self.configurar()

    def configurar(self):
        layout = [
            [sg.Button('cadastro veículos', size=(30,3))],
            [sg.Button('cadastro funcionarios', size=(30,3))],
            [sg.Button('emprestimo veículos', size=(30,3))],
            [sg.Button('Fechar', button_color=('white','red'), size=(30, 3))]
        ]
        self.__janela = sg.Window('').Layout(layout)

    def abrir(self):
        botoes, valores = self.__janela.Read()
        self.__dados_tela = botoes, valores
        return botoes, valores

    def fechar(self):
        self.__janela.Close()
