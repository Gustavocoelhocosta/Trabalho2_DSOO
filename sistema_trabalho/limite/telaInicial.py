from sistema_trabalho.limite.telaAbstract import TelaAbstract
import PySimpleGUI as sg


class TelaInicial(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}
        self.configurar()

    def configurar(self):
        layout = [
            [sg.Submit('cadastro veículos', key=0, size=(30,3))],
            [sg.Submit('cadastro funcionarios', key=1, size=(30,3))],
            [sg.Submit('emprestimo veículos', key=2, size=(30,3))]
        ]
        self.__janela = sg.Window('').Layout(layout)

    def abrir(self):
        botoes, valores = self.__janela.Read()
        return botoes, valores

    def fechar(self):
        self.__janela.Close()

