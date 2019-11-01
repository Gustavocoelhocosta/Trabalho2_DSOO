class InteiroInvalido(Exception):
    def __init__(self):
        super().__init__("O valor não é inteiro válido")

class PlacaInvalida(Exception):
    def __init__(self):
        super().__init__("formato de placa invalido")
        print("formato de placa invalido")

class VeiculoJaCadastrado(Exception):
    def __init__(self):
        super().__init__("Veículo já está cadastrado")

class VeiculoNaoCadastrado(Exception):
    def __init__(self):
        super().__init__("Veículo não está cadastrado")