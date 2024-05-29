class Region_vitivinicola:
    def __new__(cls,descripcion,nombre,provincia):
        instancia = super().__new__(cls)
        instancia.descripcion=descripcion
        instancia.nombre = nombre
        instancia.provincia=provincia
        return instancia
    
    def __init__(self,descripcion,nombre,provincia):
        self.descripcion=descripcion
        self.nombre = nombre
        self.provincia=provincia

    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, valor_descripcion):
        self.descripcion = valor_descripcion

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, valor_nombre):
        self.nombre = valor_nombre
    
    def get_provincia(self):
        return self.provincia

    def set_provincia(self, valor_provincia):
        self.provincia = valor_provincia

    def obtener_pais(self):
        if self.provincia is not None:
            return self.provincia.obtener_pais()
        