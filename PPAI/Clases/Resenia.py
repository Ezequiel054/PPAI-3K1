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

    def sos_de_periodo(self,fecha_desde,fecha_hasta,fecha_resenia):
        fecha_desde = datetime.strptime(fecha_desde, "%d-%m-%Y")
        fecha_hasta = datetime.strptime(fecha_hasta, "%d-%m-%Y")
        fecha_resenia = datetime.strptime(fecha_resenia, "%d-%m-%Y")
        if fecha_desde <= fecha_resenia <= fecha_hasta:
            return True
        return False

    def sos_de_somellier(self,sommelier):
        if self.es_premium:
            return True
        return False