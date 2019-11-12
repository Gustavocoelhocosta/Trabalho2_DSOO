from sistema_trabalho.limite.telaAbstract import TelaAbstract
import PySimpleGUI as sg


class TelaInicial(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}
        self.configurar()

    def configurar(self):
        layout = [
            [sg.Submit('Cadastro Veículos', key=0, size=(25,1))],
            [sg.Submit('Cadastro Funcionários', key=1, size=(25, 1))],
            [sg.Submit('Emprestimo Veículos', key=2, size=(25, 1))]
        ]
        self.__janela = sg.Window('').Layout(layout)

    def abrir(self):
        botoes, valores = self.__janela.Read()
        return botoes, valores

    def fechar(self):
        self.__janela.Close()

