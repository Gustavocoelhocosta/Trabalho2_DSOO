from abc import ABC, abstractmethod

class ControlaAbstract(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def abrir_tela(self):
        pass

    @abstractmethod
    def incluir(self):
        pass

    @abstractmethod
    def excluir(self):
        pass
