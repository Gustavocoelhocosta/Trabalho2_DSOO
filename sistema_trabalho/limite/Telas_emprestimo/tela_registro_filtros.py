from sistema_trabalho.limite.telaAbstract import TelaAbstract
import PySimpleGUI as sg


class TelaRegistroFiltro(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}
        self.configurar()

    def configurar(self):
        layout = [
                    [sg.Text('escolha o filtro do registro')],
                    [sg.Submit('Todos', key=0, size=(15,1))],
                    [sg.Submit('por plcaca', key=1, size=(15,1)), sg.InputText('digite a placa',size=(30,1))],
                    [sg.Submit('por matrícula', key=2, size=(15,1)),sg.InputText('digite a matrícula',size=(30,1))],
                    [sg.Submit('por motivo', key=3,size=(15,5)), sg.Listbox(values=['Acesso permitido ao veiculo', 'Matrícula não existe', 'Não possui acesso ao veículo', 'Veículo indisponível', 'Acesso Bloqueado'], size=(30,5))]
                 ]
        self.__janela = sg.Window('').Layout(layout)

    def abrir(self):
        botoes, valores = self.__janela.Read()
        return botoes, valores

    def fechar(self):
        self.__janela.Close()

