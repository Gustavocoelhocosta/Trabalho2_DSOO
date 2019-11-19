from sistema_trabalho.limite.telaAbstract import TelaAbstract
import PySimpleGUI as sg


class TelaRegistroFiltro(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}

    def configurar(self, placas):
        motivos = ['Acesso permitido ao veiculo',
                   'Matrícula não existe',
                   'Não possui acesso ao veículo',
                   'Veículo indisponível',
                   'Acesso Bloqueado']
        layout = [
                    [sg.Text('escolha o filtro do registro')],
                    [sg.Button('Todos', size=(15,1))],
                    [sg.Button('por plcaca', size=(15,1)), sg.Combo(size=(30, 1), values= placas, key='pl')],
                    [sg.Button('por matrícula', size=(15,1)),sg.InputText('',size=(30,1), key='matricula')],
                    [sg.Button('por motivo',size=(15,1)), sg.Combo(size=(30, 1), values= motivos, key='motivo')],
                    [sg.Button('voltar',size=(15,1))]
                 ]
        self.__janela = sg.Window('Registros').Layout(layout)

    def abrir(self, placas = []):
        self.configurar(placas)
        botoes, valores = self.__janela.Read()
        self.__janela.Close()
        return botoes, valores

    def fechar(self):
        self.__janela.Close()

