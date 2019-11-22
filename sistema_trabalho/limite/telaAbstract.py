from abc import ABC, abstractmethod
import PySimpleGUI as sg


class TelaAbstract(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def abrir(self):
        pass

    @abstractmethod
    def configurar(self):
        pass

    def pop_mensagem(self,mensagem):
        sg.Popup(mensagem)
