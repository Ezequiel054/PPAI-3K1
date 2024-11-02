from datetime import datetime
class Resenia:
    def __new__(cls, comentario,es_premium,fecha_resenia,puntaje,vino):
        instancia = super().__new__(cls)
        instancia.comentario = comentario
        instancia.es_premium= es_premium
        instancia.fecha_resenia=fecha_resenia
        instancia.puntaje=puntaje
        instancia.vino=vino
        return instancia
    
    def __init__(self,comentario,es_premium,fecha_resenia,puntaje,vino):
        self.comentario = comentario
        self.es_premium = es_premium
        self.fecha_resenia = fecha_resenia
        self.puntaje = puntaje
        self.vino=vino

    def get_comentario(self):
        return self.comentario

    def set_comentario(self, valor_comentario):
        self.comentario = valor_comentario

    def get_es_premium(self):
        return self.es_premium

    def set_es_premium(self, valor_es_premium):
        self.es_premium = valor_es_premium

    def get_fecha_resenia(self):
        return self.fecha_resenia

    def set_fecha_resenia(self, valor_fecha_resenia):
        self.fecha_resenia = valor_fecha_resenia

    def get_puntaje(self):
        return self.puntaje

    def set_puntaje(self, valor_puntaje):
        self.puntaje = valor_puntaje

    def get_vino(self):
        return self.vino

    def set_vino(self, valor_vino):
        self.vino = valor_vino

    # Esta función verifica si una fecha de reseña está dentro de un período de tiempo especificado (fecha_desde y fecha_hasta).
    # Convierte las fechas de formato de cadena a objetos datetime y devuelve True si la fecha de la reseña está dentro del rango, de lo contrario, devuelve False.
    def sos_de_periodo(self,fecha_desde,fecha_hasta,fecha_resenia):
        fecha_desde = datetime.strptime(fecha_desde, "%d-%m-%Y")
        fecha_hasta = datetime.strptime(fecha_hasta, "%d-%m-%Y")
        fecha_resenia = datetime.strptime(fecha_resenia, "%d-%m-%Y")
        if fecha_desde <= fecha_resenia <= fecha_hasta:
            return True
        return False

    # Esta función verifica si una reseña es de un sommelier premium.
    # Devuelve True si la reseña es premium y el sommelier especificado es "Sommelier", de lo contrario, devuelve False.
    def sos_de_somellier(self,sommelier):
        if self.es_premium and sommelier=="Sommelier":
            return True
        return False