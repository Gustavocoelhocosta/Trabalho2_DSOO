from sistema_trabalho.limite.telaAbstract import TelaAbstract
import PySimpleGUI as sg


class TelaRegistroLista(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}
        self.configurar ()

    def configurar(self, registros = []):
        layout = [
            [sg.Text('lista de registros')],
            [sg.Listbox(values = registros, size=(65,10))],
            [sg.Exit('Fechar',size=(10,2))]
             ]
        self.__janela = sg.Window('').Layout(layout)

    def abrir(self, registros):
        self.configurar(registros)
        self.__dados_tela = self.__janela.Read()
        botoes, valores = self.__dados_tela
        self.__janela.Close()
        return botoes, valores

    def fechar(self):
        self.__janela.Close()

