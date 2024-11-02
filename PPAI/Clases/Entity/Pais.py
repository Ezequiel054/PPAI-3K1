class Pais:
    def __new__(cls,nombre,provincia):
        instancia = super().__new__(cls)
        instancia.nombre = nombre
        instancia.provincia=provincia
        return instancia
    
    def __init__(self,nombre,provincia):
        self.nombre = nombre
        self.provincia=provincia

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, valor_nombre):
        self.nombre = valor_nombre

    def get_provincia(self):
        return self.provincia

    def set_provincia(self, valor_provincia):
        self.provincia = valor_provincia