from sistema_trabalho.limite.telaAbstract import TelaAbstract


class TelaVeiculo(TelaAbstract):
    def listar_opcoes(self):
        print('Escolha dentre as opções')
        print('0 - incluir veículo')
        print('1 - excluir veículo')
        print('2 - listar veículos')
        print('3 - voltar')
        return self.pedir_inteiro_valido('digite uma opção ', [0,1,2,3], 'não é uma opção válida')

    def pedir_dados_veiculo(self):
        print('insira os dados do veículo')
        dados = []
        dados.append(self.pedir_placa())
        dados.append(input('digite o modelo - ').upper())
        dados.append(input('digite a marca - ').upper())
        dados.append(self.pedir_inteiro_valido('digite o ano de fabricação - '))
        dados.append(self.pedir_inteiro_valido('digite a quilometragem atual - '))
        return dados








