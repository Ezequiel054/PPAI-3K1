class Varietal:
    def __new__(cls, descripcion,porcentaje_composicion):
        instancia = super().__new__(cls)
        instancia.descripcion = descripcion
        instancia.porcentajeComposicion= porcentaje_composicion
        return instancia
    
    def __init__(self,descripcion,porcentaje_composicion):
        self.descripcion = descripcion
        self.porcentajeComposicion = porcentaje_composicion

    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, valor_descripcion):
        self.descripcion = valor_descripcion

    def get_porcentaje_composicion(self):
        return self.porcentaje_composicion

    def set_porcentaje_composicion(self, valor_porcentaje_comision):
        self.porcentaje_composicion = valor_porcentaje_comision