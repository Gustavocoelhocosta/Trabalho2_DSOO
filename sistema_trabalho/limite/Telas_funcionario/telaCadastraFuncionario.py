import PySimpleGUI as sg
from sistema_trabalho.limite.telaAbstract import TelaAbstract

class TelaIncluirFuncionario(TelaAbstract):
    def __init__(self):
        self.__janela = None
        self.__dados_tela = dict()

    def configurar(self, dados_funcionario, cargos = []):
        layout = [
            [sg.Text('Entre com os dados do funcionário')],
            [sg.Text('Matrícula', size=(18, 1)), sg.InputText(dados_funcionario['matricula'], key='matricula')],
            [sg.Text('Nome', size=(18,1)), sg.InputText(dados_funcionario['nome'], key='nome')],
            [sg.Text('Data de nascimento', size=(18, 1)), sg.InputText(dados_funcionario['nascimento'], key='nascimento')],
            [sg.Text('Telefone', size=(18, 1)), sg.InputText(dados_funcionario['telefone'], key='telefone')],
            [sg.Text('Cargo', size=(18, 1)), sg.Combo(size=(18, 1),default_value=dados_funcionario['cargo'], values= cargos, key='cargo')],
            [sg.Button('Incluir'), sg.Cancel('Voltar')]
            ]
        self.__janela = sg.Window('', layout)

    def abrir(self, dados_funcionario = None, cargos = []):
        if not dados_funcionario:
            dados = {'matricula': '', 'nome': '', 'nascimento': '', 'telefone': '', 'cargo': ''}
        else:
            dados = dados_funcionario
        self.configurar(dados, cargos)
        self.__dados_tela = self.__janela.Read()
        botoes, valores = self.__dados_tela
        self.__janela.Close()
        return botoes, valores

    def pop_mensagem(self, mensagem):
        sg.Popup(mensagem)

    def voltar(self):
        self.__janela.Close()