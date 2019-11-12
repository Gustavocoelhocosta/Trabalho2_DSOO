from abc import ABC, abstractclassmethod

class ControlaAbstract(ABC):

    @abstractclassmethod
    def abrir_tela(self):
        pass

    @abstractclassmethod
    def incluir(self):
        pass

    @abstractclassmethod
    def excluir(self):
        pass
