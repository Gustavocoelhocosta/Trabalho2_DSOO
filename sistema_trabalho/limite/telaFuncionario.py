from sistema_trabalho.limite.telaAbstract import TelaAbstract


class TelaFuncionario(TelaAbstract):
    def listar_opcoes(self):
        print('Escolha dentre as opções')
        print('0 - incluir funcionário')
        print('1 - excluir funcionário')
        print('2 - listar funcionários')
        print('3 - cadastrar veículo no funcionário')
        print('4 - excluir veículo do funcionário')
        print('5 - listar veículos permitidos')
        print('6 - voltar')
        return self.pedir_inteiro_valido('Digite o numero da opção escolhida - ', [0, 1, 2, 3, 4, 5, 6])

    def cadastrar_funcionario(self):
        print('Cadastrar novo funcionário')
        dados = list()
        dados.append(self.pedir_matricula())
        dados.append(input('Digite o nome: ').upper())
        dados.append(self.pedir_inteiro_valido('Digite a data de nascimento (ddmmaaaa): '))
        dados.append(self.pedir_inteiro_valido('Digite o telefone: '))
        dados.append(input('Digite o cargo: ').upper())
        return dados

    def listar_funcionarios(self, lista):
        print('MATRÍCULA - NOME - DATA NASCIMENTO - TELEFONE - CARGO')
        for funcionario in lista:
            print('%d - %s - %s - %s - %s'% (lista[funcionario].matricula,
                                             lista[funcionario].nome,
                                             lista[funcionario].data_de_nascimento,
                                             lista[funcionario].telefone,
                                             lista[funcionario].cargo))
