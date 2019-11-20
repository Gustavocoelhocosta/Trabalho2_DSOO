

class DadosIncorretos(Exception):
    def __init__(self):
        super().__init__('Dados incorretos')
