class VeiculoJaCadastrado(Exception):
    def __init__(self):
        super().__init__("não foi possível cadastrar veículo pois já existe veículo com a mesma placa")