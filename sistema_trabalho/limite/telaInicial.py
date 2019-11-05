from sistema_trabalho.limite.telaAbstract import TelaAbstract
import PySimpleGUI as sg


class TelaInicial(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}
        self.configurar()

    def configurar(self):
        layout = [
            [sg.Submit('cadastro veículos', key=0)],
            [sg.Submit('cadastro funcionarios', key=1)],
            [sg.Submit('emprestimo veículos', key=2)]
        ]
        self.__janela = sg.Window('').Layout(layout)

    def abrir(self):

        botoes, valores = janela.Read()
        return botoes



