from sistema_trabalho.limite.telaAbstract import TelaAbstract
import PySimpleGUI as sg


class TelaDevolver(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}

    def configurar(self, placas):
        layout = [
            [sg.Text('placa', size=(17,1)), sg.Combo(size=(12, 1), values= placas, key='pl')],
            [sg.Text('quilometragem rodada', size=(17,1)), sg.InputText(size=(12, 1), key='km')],
            [sg.Button('devolver', size=(12, 2)), sg.Button('voltar', size=(12, 2))]
                 ]
        self.__janela = sg.Window('Empréstimo').Layout(layout)

    def abrir(self, placas=[]):
        self.configurar(placas)
        botoes, valores = self.__janela.Read()
        self.__janela.Close()
        return botoes, valores

    def fechar(self):
        self.__janela.Close()
