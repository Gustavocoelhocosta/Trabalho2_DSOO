from sistema_trabalho.limite.telaAbstract import TelaAbstract
import PySimpleGUI as sg


class TelaVeiculo(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}
        self.configurar()

    def configurar(self):
        layout = [
            [sg.Submit('incluir veículo', key=0)],
            [sg.Submit('excluir veículo', key=1)],
            [sg.Submit('alterar veículos', key=2)],
            [sg.Submit('listar veículos', key=3)],
            [sg.Submit('voltar', key=4)]
        ]
        self.__janela = sg.Window('Cadastro Veículo').Layout(layout)


    def abrir(self):
        self.__dados_tela = self.__janela.Read()
        botoes, valores = self.__janela.Read()
        if botoes:
            return self.fechar()
        return botoes, valores










