class Bodega:
    def __new__(cls,coordenas_ubicacion,descripcion,fecha_ultima_actualizacion,historia,nombre,periodo_actualizacion,region):
        instancia = super().__new__(cls)
        instancia.coordenas_ubicacion=coordenas_ubicacion
        instancia.descripcion=descripcion
        instancia.fecha_ultima_actualizacion=fecha_ultima_actualizacion
        instancia.historia=historia
        instancia.nombre = nombre
        instancia.periodo_actualizacion=periodo_actualizacion
        instancia.region=region
        return instancia
    
    def __init__(self,coordenas_ubicacion,descripcion,fecha_ultima_actualizacion,historia,nombre,periodo_actualizacion,region):
        self.coordenas_ubicacion=coordenas_ubicacion
        self.descripcion=descripcion
        self.fecha_ultima_actualizacion=fecha_ultima_actualizacion
        self.historia=historia
        self.nombre = nombre
        self.periodo_actualizacion=periodo_actualizacion
        self.region=region

    def get_coordenadas_ubicacion(self):
        return self.coordenadas_ubicacion

    def set_coordenadas_ubicacion(self, valor_coordenadas_ubicacion):
        self.coordenadas_ubicacion = valor_coordenadas_ubicacion

    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, valor_descripcion):
        self.descripcion = valor_descripcion

    def get_fecha_ultima_actualizacion(self):
        return self.fecha_ultima_actualizacion

    def set_fecha_ultima_actualizacion(self, valor_fecha_ultima_actualizacio):
        self.fecha_ultima_actualizacion = valor_fecha_ultima_actualizacio

    def get_historia(self):
        return self.historia

    def set_historia(self, valor_historia):
        self.historia = valor_historia

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, valor_nombre):
        self.nombre = valor_nombre

    def get_periodo_actualizacion(self):
        return self.periodo_actualizacion

    def set_periodo_actualizacion(self, valor_periodo_actualizacion):
        self.periodo_actualizacion = valor_periodo_actualizacion
    
    def get_region(self):
        return self.region

    def set_region(self, valor_region):
        self.region = valor_region
    
    def obtener_region_y_pais(self):
        return self.region.get_nombre(), self.region.obtener_pais()