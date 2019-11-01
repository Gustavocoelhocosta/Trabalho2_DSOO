from sistema_trabalho.limite.telaAbstract import TelaAbstract

class TelaEmprestimo(TelaAbstract):
    def listar_opcoes(self):
        print('Escolha dentre as opções')
        print('0 - retirar veículo')
        print('1 - devolver veículo')
        print('2 - listar registros')
        print('3 - voltar')
        return self.pedir_inteiro_valido('digite uma opção ', [0,1,2,3], 'não é uma opção válida')


    def retirar_veiculo(self):
        print('Emprestimo de veículo')
        return self.pedir_matricula()


    def pedir_matricula(self):
        return self.pedir_inteiro_valido('digite a matricula - ')

    def devolver_veiculo(self):
        print('Devolução de veículo')
        dados = []
        dados.append(self.pedir_placa())
        dados.append(self.pedir_inteiro_valido('digite quilometros rodados - '))
        return dados

    def listar_filtro_registro(self):
        print('----------------------------------------------------')
        print('Escolha o filtro do registro')
        print('0 - por motivo/permissão')
        print('1 - por matrícula do funcionario')
        print('2 - por placa do veículo')
        print('3 - todos os registros')
        print('4 - voltar')
        filtro = self.pedir_inteiro_valido('digite uma opção ', [0,1,2,3,4], 'não é uma opção válida')
        print('----------------------------------------------------')
        if filtro == 0:
            print('Escolha o motivo')
            print('0 - Acesso permitido ao veiculo')
            print('1 - Matrícula não existe')
            print('2 - Não possui acesso ao veículo')
            print('3 - veículo indisponível')
            print('4 - voltar')
            motivo = self.pedir_inteiro_valido('digite uma opção ', [0,1,2,3,4], 'não é uma opção válida')
            return [0, motivo]
        elif filtro == 1:
            #listar todos os funcionarios
            return [1, self.pedir_matricula()]
        elif filtro == 2:
            #listar todas as placas
            return [2, self.pedir_placa()]
        else:
            return [filtro, None]

    def listar_registros(self, lista):
        print('PLACA - NOME - MOTIVO - DATA/HORA')
        for registro in lista:
            if registro.veiculo == None:
                if registro.funcionario == None:
                    print('vazio - vazio' + ' - ' + str(registro.motivo) + ' - ' + str(registro.data_hora))
                else:
                    print('vazio - ' + str(registro.funcionario.nome) + ' - ' + str(registro.motivo) + ' - ' + str(registro.data_hora))
            else:
                print(str(registro.veiculo.placa) + ' - ' + str(registro.funcionario.nome) + ' - ' + str(registro.motivo) + ' - ' + str(registro.data_hora))
