from abc import ABC, abstractmethod
from typing import List

class IIterador(ABC):
    @abstractmethod
    def actual(self):
        pass
    
    def cumpleFiltro(self, filtros: List[object]):
        pass
    
    @abstractmethod
    def haTerminado(self):
        pass
    
    @abstractmethod
    def primero(self) -> None:
        pass
    
    @abstractmethod
    def siguiente(self) -> None:
        pass
