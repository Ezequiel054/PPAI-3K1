from Clases.Interface.IIterador import IIterador
from typing import List, Dict


class IteradorResenias(IIterador):
    def __init__(self, resenias, filtros):
        self._resenias = resenias
        self._filtros = filtros
        self._pos_actual = 0

    def actual(self) -> object:
        if not self.haTerminado():
            return self._resenias[self._pos_actual]
        raise IndexError("Iterator has finished.")
    
    def cumpleFiltro(self) -> bool:
        resenia_actual = self.actual()
        
        # Extraer filtros para validarlos en la reseña actual
        fecha_desde = self._filtros.get("fecha_desde")
        fecha_hasta = self._filtros.get("fecha_hasta")
        sommelier = self._filtros.get("sommelier")
        
        # Verificar si la reseña cumple con el periodo y el sommelier
        cumple_fecha = resenia_actual.sos_de_periodo(fecha_desde, fecha_hasta, resenia_actual.get_fecha_resenia())
        cumple_sommelier = resenia_actual.sos_de_somellier(sommelier)
        
        return cumple_fecha and cumple_sommelier
    
    def haTerminado(self) -> bool:
        return self._pos_actual >= len(self._resenias)
    
    def primero(self) -> None:
        self._pos_actual = 0
    
    def siguiente(self) -> None:
        if not self.haTerminado():
            self._pos_actual += 1
    def new(self, resenias: List[object], filtros: Dict) -> None:
        self._resenias = resenias
        self._filtros = filtros
        self._pos_actual = 0
        
    def set_filtros(self, filtros: dict) -> None:
        self._filtros = filtros