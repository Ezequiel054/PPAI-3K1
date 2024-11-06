from abc import ABC, abstractmethod
from Clases.Interface import IIterador

class IAgregado(ABC):
    @abstractmethod
    def crearIterador(self, elementos) -> IIterador:
        pass