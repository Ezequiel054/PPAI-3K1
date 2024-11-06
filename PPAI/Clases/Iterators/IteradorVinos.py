from Clases.Interface.IIterador import IIterador
from typing import List

class IteradorVinos(IIterador):
    def __init__(self, vinos, filtros):
        self._vinos = vinos
        self._filtros = filtros
        self._pos_actual = 0

    def actual(self) -> object:
        if not self.haTerminado():
            return self._vinos[self._pos_actual]
        raise IndexError("Iterator has finished.")
    
    def cumpleFiltro(self) -> bool:
        vino_actual = self.actual()
        cumple = True

        # Aplicar los filtros uno por uno al vino actual
        if "fecha_desde" in self._filtros and "fecha_hasta" in self._filtros:
            cumple = cumple and any(
                resenia.sos_de_periodo(self._filtros["fecha_desde"], self._filtros["fecha_hasta"], resenia.get_fecha_resenia())
                for resenia in vino_actual.get_resenia()
            )
        
        if "sommelier" in self._filtros:
            cumple = cumple and any(
                resenia.sos_de_somellier(self._filtros["sommelier"])
                for resenia in vino_actual.get_resenia()
            )

        return cumple
    
    def haTerminado(self) -> bool:
        return self._pos_actual >= len(self._vinos)
    
    def primero(self) -> None:
        self._pos_actual = 0
    
    def siguiente(self) -> None:
        if not self.haTerminado():
            self._pos_actual += 1
            
    def new(self, vinos: List[object], filtros: List[object]) -> None:
        self._vinos = vinos
        self._filtros = filtros
        self._pos_actual = 0
    
    def set_filtros(self, filtros: dict) -> None:
        self._filtros = filtros
