from sistema_trabalho.limite.telaAbstract import TelaAbstract
import PySimpleGUI as sg

class TelaIncluirVeiculo(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = {}


    def configurar(self, dados_veiculos):
        layout = [
                [sg.Text('Entre com os dados do veículo')],
                [sg.Text('Placa', size=(15, 1)), sg.InputText(dados_veiculos['placa'], key='placa')],
                [sg.Text('Modelo', size=(15, 1)), sg.InputText(dados_veiculos['modelo'],key='modelo')],
                [sg.Text('Marca', size=(15, 1)), sg.InputText(dados_veiculos['marca'], key='marca')],
                [sg.Text('Ano', size=(15, 1)), sg.InputText(str(dados_veiculos['ano']), key='ano')],
                [sg.Text('Kilometragem', size=(15, 1)), sg.InputText(str(dados_veiculos['km']), key='quilometragem_atual')],
                [sg.Submit('incluir'), sg.Cancel('Voltar')]
                ]
        self.__janela = sg.Window('').Layout(layout)

    def abrir(self, dados_veiculo = None):
        if not dados_veiculo:
            dados = {'placa': '', 'modelo': '', 'marca': '', 'ano': '', 'km': ''}
        else:
            dados = dados_veiculo
        self.configurar(dados)
        self.__dados_tela = self.__janela.Read()
        botoes, valores = self.__dados_tela
        self.__janela.Close()
        return botoes, valores


    def pop_mensagem(self,mensagem):
        sg.Popup(mensagem)
