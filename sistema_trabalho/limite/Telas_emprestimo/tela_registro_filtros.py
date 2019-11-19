from sistema_trabalho.limite.telaAbstract import TelaAbstract
import PySimpleGUI as sg


class TelaRegistroFiltro(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}

    def configurar(self):
        motivos = ['Acesso permitido ao veiculo',
                   'Matrícula não existe',
                   'Não possui acesso ao veículo',
                   'Veículo indisponível',
                   'Acesso Bloqueado']
        layout = [
                    [sg.Text('escolha o filtro do registro')],
                    [sg.Button('Todos', size=(15,1))],
                    [sg.Button('por plcaca', size=(15,1)), sg.InputText('digite a placa',size=(30,1))],
                    [sg.Button('por matrícula', size=(15,1)),sg.InputText('digite a matrícula',size=(30,1))],
                    [sg.Button('por motivo',size=(15,5)), sg.Listbox(values=motivos, size=(30,5))],
                    [sg.Button('voltar',size=(15,1))]
                 ]
        self.__janela = sg.Window('').Layout(layout)

    def abrir(self):
        self.configurar()
        botoes, valores = self.__janela.Read()
        self.__janela.Close()
        return botoes, valores

    def fechar(self):
        self.__janela.Close()

