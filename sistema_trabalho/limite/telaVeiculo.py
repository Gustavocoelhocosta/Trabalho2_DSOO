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
        return botoes

class TelaIncluirVeiculo(TelaAbstract):
    def incluir_veiculo(self):
        layout = [
            [sg.Text('Entre com os dados do veículo')],
            [sg.Text('Placa', size=(15, 1)), sg.In(key='placa')],
            [sg.Text('Modelo', size=(15, 1)), sg.InputText(key='modelo')],
            [sg.Text('Marca', size=(15, 1)), sg.InputText()],
            [sg.Text('Ano', size=(15, 1)), sg.InputText()],
            [sg.Text('Kilometragem', size=(15, 1)), sg.InputText()],
            [sg.Submit('incluir'), sg.Cancel('Voltar')]
        ]
        janela = sg.Window('').Layout(layout)
        # while True:
        botoes, valores = janela.Read()
            # try:
            #     int(valores['placa'])

        return valores

    # def listar_opcoes(self):
    #     print('Escolha dentre as opções')
    #     print('0 - incluir veículo')
    #     print('1 - excluir veículo')
    #     print('2 - listar veículos')
    #     print('3 - voltar')
    #     return self.pedir_inteiro_valido('digite uma opção ', [0,1,2,3], 'não é uma opção válida')

    def pedir_dados_veiculo(self, dados = {}):
        print('insira os dados do veículo')
        dados = []
        dados.append(self.pedir_placa())
        dados.append(input('digite o modelo - ').upper())
        dados.append(input('digite a marca - ').upper())
        dados.append(self.pedir_inteiro_valido('digite o ano de fabricação - '))
        dados.append(self.pedir_inteiro_valido('digite a quilometragem atual - '))
        return dados








