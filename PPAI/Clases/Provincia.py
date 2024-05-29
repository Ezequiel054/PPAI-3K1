class Provincia:
    def __new__(cls,nombre,region_vitivinicola,pais):
        instancia = super().__new__(cls)
        instancia.nombre = nombre
        instancia.region_vitivinicola=region_vitivinicola
        instancia.pais=pais
        return instancia
    
    def __init__(self,nombre,region_vitivinicola,pais):
        self.nombre = nombre
        self.region_vitivinicola=region_vitivinicola
        self.pais=pais

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, valor_nombre):
        self.nombre = valor_nombre

    def get_region_vitivinicola(self):
        return self.region_vitivinicola

    def set_region_vitivinicola(self, valor_region_vitivinicola):
        self.region_vitivinicola = valor_region_vitivinicola
    
    def get_pais(self):
        return self.pais

    def set_pais(self, valor_pais):
        self.pais = valor_pais

    # Esta función obtiene y retorna el nombre del país asociado a la instancia actual.
    # Llama al método `get_nombre` del atributo `pais` y retorna su valor.
    def obtener_pais(self):
        return self.pais.get_nombre()