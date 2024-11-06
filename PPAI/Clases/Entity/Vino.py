from Clases.Interface.IAgregado import IAgregado
from Clases.Iterators.IteradorResenias import IteradorResenias
from Clases.Entity.Resenia import Resenia


class Vino(IAgregado):

    def __new__(cls, aniada, fecha_actualizacion, imagen_etiqueta, nombre, nota_de_cata_bodega, precio_ars, bodega, varietal, resenia):
        instancia = super().__new__(cls)
        instancia.aniada = aniada
        instancia.fecha_actualizacion = fecha_actualizacion
        instancia.imagen_etiqueta = imagen_etiqueta
        instancia.nombre = nombre
        instancia.nota_de_cata_bodega = nota_de_cata_bodega
        instancia.precio_ars = precio_ars
        instancia.bodega = bodega
        instancia.varietal = varietal
        instancia.resenia = resenia
        return instancia
    
    def __init__(self, aniada, fecha_actualizacion, imagen_etiqueta, nombre, nota_de_cata_bodega, precio_ars, bodega, varietal, resenia):
        self.aniada = aniada
        self.fecha_actualizacion = fecha_actualizacion
        self.imagen_etiqueta = imagen_etiqueta
        self.nombre = nombre
        self.nota_de_cata_bodega = nota_de_cata_bodega
        self.precio_ars = precio_ars
        self.bodega = bodega
        self.varietal = varietal
        self.resenia = resenia

    def get_aniada(self):
        return self.aniada

    def set_aniada(self, valor_aniada):
        self.aniada = valor_aniada

    def get_fecha_actualizacion(self):
        return self.fecha_actualizacion

    def set_fecha_actualizacion(self, valor_fecha_actualizacion):
        self.fecha_actualizacion = valor_fecha_actualizacion

    def get_imagen_etiqueta(self):
        return self.imagen_etiqueta

    def set_imagen_etiqueta(self, valor_imagen_etiqueta):
        self.imagen_etiqueta = valor_imagen_etiqueta

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, valor_nombre):
        self.nombre = valor_nombre

    def get_nota_de_cata_bodega(self):
        return self.nota_de_cata_bodega

    def set_nota_de_cata_bodega(self, valor_nota_de_cata_bodega):
        self.nota_de_cata_bodega = valor_nota_de_cata_bodega

    def get_precio_ars(self):
        return self.precio_ars

    def set_precio_ars(self, valor_precio_ars):
        self.precio_ars = valor_precio_ars

    def get_bodega(self):
        return self.bodega
    
    def set_bodega(self, valor_bodega):
        self.bodega = valor_bodega

    def get_varietal(self):
        return self.varietal
    
    def set_varietal(self, valor_varietal):
        self.varietal = valor_varietal

    def get_resenia(self):
        return self.resenias if self.resenias is not None else []
    
    def set_resenia(self, valor_resenia):
        self.resenia = valor_resenia
    
    # Esta función obtiene las reseñas de un vino en un período de tiempo específico realizadas por un sommelier en particular.
    # Si no hay reseñas que cumplan con los criterios, retorna False y una lista vacía.
    # Si hay reseñas que cumplan con los criterios, retorna True y la lista de reseñas.
    """
    def tenes_resenias_de_tipo_en_periodo(self,vino,fecha_desde,fecha_hasta,sommelier):
        resenias = []
        for resenia in vino.get_resenia():
            if resenia.sos_de_periodo(fecha_desde, fecha_hasta, resenia.get_fecha_resenia()):
                if resenia.sos_de_somellier(sommelier):
                    resenias.append(resenia)
        if len(resenias) == 0: 
            return False, []
        else:
            return True, resenias
    """
    def tenes_resenias_de_tipo_en_periodo(self, vino, fecha_desde, fecha_hasta, sommelier):
        resenias = vino.get_resenia()  # Obtener todas las reseñas del vino
        iterador_resenia = self.crearIterador(resenias)  # Crear el iterador con filtros
        iterador_resenia.set_filtros({
            "fecha_desde": fecha_desde,
            "fecha_hasta": fecha_hasta,
            "sommelier": sommelier
        })
        iterador_resenia.primero()  # Iniciar desde la primera reseña
        
        resenias_filtradas = []  # Lista para almacenar las reseñas que cumplen con los filtros
        
        while not iterador_resenia.haTerminado():
            if iterador_resenia.cumpleFiltro():
                resenias_filtradas.append(iterador_resenia.actual())
            iterador_resenia.siguiente()
        
        return (True, resenias_filtradas) if resenias_filtradas else (False, [])
    
    # Esta función obtiene y retorna el nombre de la bodega asociada a la instancia actual.
    def buscar_info_bodega(self):
        return self.bodega.get_nombre()
    
    # Esta función obtiene y retorna una lista de descripciones de los varietales de un vino.
    def buscar_varietal(self,vino):
        varietales=[]
        for varietal in vino.get_varietal():
            varietales.append(varietal.get_descripcion())
        return varietales

    # Esta función calcula y retorna el puntaje promedio de una lista de puntajes.
    # La lista de puntajes puede contener sublistas de puntajes.
    # Si no hay puntajes, retorna 0. Si hay puntajes, retorna el promedio con dos decimales.
    def calcular_puntaje_promedio(self,puntajes):
        if not puntajes: 
            return 0
    
        puntajes_totales = []
        for sublista in puntajes:
            if isinstance(sublista, list):
                puntajes_totales.extend(sublista)
            else:
                puntajes_totales.append(sublista)

        if not puntajes_totales:
            return 0

        promedio_general = sum(puntajes_totales) / len(puntajes_totales)
        promedio_general = "{:.2f}".format(promedio_general)
        return promedio_general

    # Esta función obtiene y retorna una lista de puntajes de reseñas de un vino en un período de tiempo específico realizadas por un sommelier en particular.
    """
    def calcular_puntaje_de_sommelier_en_periodo(self,vino,fecha_desde,fecha_hasta,sommelier):
        puntaje_resenias=[]
        for resenia in vino.get_resenia():
            if resenia.sos_de_periodo(fecha_desde, fecha_hasta, resenia.get_fecha_resenia()):
                if resenia.sos_de_somellier(sommelier):
                    puntaje_resenias.append(resenia.get_puntaje())
        return puntaje_resenias
    """
    def calcular_puntaje_de_sommelier_en_periodo(self, vino, fecha_desde, fecha_hasta, sommelier):
        puntaje_resenias = []

        # Crear el iterador para las reseñas del vino
        iterador_resenias = IteradorResenias(vino.get_resenia(),filtros=[])
        
        # Establecer los filtros en el iterador
        iterador_resenias.set_filtros({
            "fecha_desde": fecha_desde,
            "fecha_hasta": fecha_hasta,
            "sommelier": sommelier
        })
        
        iterador_resenias.primero()  # Iniciar desde la primera reseña

        while not iterador_resenias.haTerminado():
            if iterador_resenias.cumpleFiltro():
                resenia = iterador_resenias.actual()  # Obtener la reseña que cumple con los filtros
                puntaje_resenias.append(resenia.get_puntaje())  # Agregar el puntaje de la reseña
            iterador_resenias.siguiente()  # Avanzar a la siguiente reseña

        return puntaje_resenias


    def crearIterador(self, elementos):
        if not elementos:
            raise ValueError("La lista de elementos no puede estar vacía.")

        # Verificar el tipo de elemento para decidir qué iterador crear
        if isinstance(elementos[0], Resenia):
            return IteradorResenias(elementos, filtros=[])  # Retorna un iterador de resenia con filtros vacíos
        else:
            raise ValueError("Tipo de elemento no soportado.")