class InteiroInvalido(Exception):
    def __init__(self):
        super().__init__("O valor não é inteiro válido")

class DadosVeiculoInvalidos(Exception):
    def __init__(self):
        super().__init__("dados do veículo invalidos")

class VeiculoJaCadastrado(Exception):
    def __init__(self):
        super().__init__("Veículo já está cadastrado")

class MatriculaNaoExiste(Exception):
    def __init__(self):
        super().__init__("Matrícula não existe")

class NaoPossuiAcessoAoVeiculo(Exception):
    def __init__(self):
        super().__init__("Não possui acesso ao veículo")


class VeiculoIndisponivel(Exception):
    def __init__(self):
        super().__init__("veículo indisponível")

class AcessoBloqueado(Exception):
    def __init__(self):
        super().__init__("Acesso Bloqueado")
