from tkinter import *
from tkinter import messagebox,ttk,simpledialog,font
from Datos.ConexionDb import ConexionDB
from Clases.Interface.IAgregado import IAgregado  # Ensure IAgregado is correctly defined and imported
from Clases.Iterators.IteradorVinos import IteradorVinos
from Clases.Entity.Vino import Vino
from Datos.datos import carga_datos


class Gestor_ranking_vinos(IAgregado):
    _vinos = None
    def __new__(cls):
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self):
        self._db = ConexionDB()
        self.db.crear_tablas()
        self._vinos = carga_datos()
        self.db.insertar_datos(self._vinos)
    
    @property
    def db(self):
        return self._db

    def obtener_vinos(self):
        # Usamos el método consultar_vinos de la base de datos
        return self.db.consultar_vinos()
    
    def opcion_generar_ranking_vinos(self):
        pass

    def tomar_sel_fecha_desde_y_hasta(self,fecha_desde,fecha_hasta):
        return fecha_desde,fecha_hasta
    
    def tomar_sel_tipo_resenia(self,resenia):
        return resenia
    
    def tomar_sel_tipo_visualizacion(self,visualizacion):
        return visualizacion
    
    def tomar_confirmacion_gen_reporte(self,confirmacion):
        return confirmacion
    
    # --------------------------------------------------------------------------------------------------------------------
    
    # Esta función busca vinos con reseñas en un período específico hechas por un sommelier.
    # Filtra los vinos que tienen reseñas en el período y construye una lista con la información relevante de estos vinos.
    # Si no hay reseñas en el período, muestra un mensaje informativo y retorna False y una lista vacía.
    # Si hay reseñas en el período, retorna una lista de información de los vinos, una lista de vinos filtrados y las reseñas del período.
    ############################
    ######## ITERATOR 1 ########      
    ############################
    # Antes
    """
    def buscar_vinos_con_resenias_en_periodo(self,vinos,fecha_desde,fecha_hasta,sommelier):
        vinos_con_resenias_periodo = []
        vinos_filtrados = []
        for vino in vinos:
            tiene_resenias, resenias_periodo = vino.tenes_resenias_de_tipo_en_periodo(vino, fecha_desde, fecha_hasta, sommelier)
            if tiene_resenias:
                varietales = vino.buscar_varietal(vino)
                vinos_con_resenias_periodo.append([vino.get_nombre(), vino.get_precio_ars(), vino.buscar_info_bodega(), vino.bodega.obtener_region_y_pais(), varietales])
                vinos_filtrados.append(vino) 
        if not vinos_con_resenias_periodo:
            messagebox.showinfo("Información", "No reseñas creadas por Sommeliers.")
            return False, []
        return vinos_con_resenias_periodo, vinos_filtrados,resenias_periodo
    """
    # Ahora
    def buscar_vinos_con_resenias_en_periodo(self, vinos, fecha_desde, fecha_hasta, sommelier):
        vinos_con_resenias_periodo = []
        vinos_filtrados = []
        resenias_periodo = [] 
        
        # Creamos el iterador con los filtros adecuados
        iterador_vinos = self.crearIterador(vinos)
        iterador_vinos.set_filtros({
            "fecha_desde": fecha_desde,
            "fecha_hasta": fecha_hasta,
            "sommelier": sommelier
        })
        iterador_vinos.primero()

        while not iterador_vinos.haTerminado():
            vino = iterador_vinos.actual() # Obtenemos el vino actual
            tiene_resenias, resenias_periodo_vino = vino.tenes_resenias_de_tipo_en_periodo(vino,fecha_desde, fecha_hasta, sommelier)
            if iterador_vinos.cumpleFiltro(): # restringuimos en base a los filtros
                varietales = vino.buscar_varietal(vino)
                vinos_con_resenias_periodo.append([
                    vino.get_nombre(),
                    vino.get_precio_ars(),
                    vino.buscar_info_bodega(),
                    vino.bodega.obtener_region_y_pais(),
                    varietales
                ])
                vinos_filtrados.append(vino)
                resenias_periodo.extend(resenias_periodo_vino)
                
            iterador_vinos.siguiente() # Avanzamos al siguiente vino

        if not vinos_con_resenias_periodo:
            messagebox.showinfo("Información", "No reseñas creadas por Sommeliers.")
            return False, [], []
        
        return vinos_con_resenias_periodo, vinos_filtrados, resenias_periodo
    
    # Esta función calcula los puntajes de sommelier en un período específico para una lista de vinos filtrados.
    # Para cada vino, obtiene las reseñas en el período, calcula el promedio de puntajes y agrega estos datos a las listas correspondientes.
    # Retorna dos listas: una con los puntajes y otra con los puntajes promedio de los sommeliers.
    ############################
    ######## ITERATOR 2 ########      
    ############################
    # Antes
    """
    def calcular_puntaje_de_sommelier_en_periodo(self,vinos_filtrados,fecha_desde,fecha_hasta,sommelier):
        puntajes_sommelier_promedio=[]
        puntajes=[]
        for vino in vinos_filtrados:
            puntaje_resenias=vino.calcular_puntaje_de_sommelier_en_periodo(vino,fecha_desde,fecha_hasta,sommelier)
            puntajes.append(puntaje_resenias)
            puntajes_sommelier_promedio.append(vino.calcular_puntaje_promedio(puntaje_resenias))
        return puntajes,puntajes_sommelier_promedio
    """
    # Ahora
    def calcular_puntaje_de_sommelier_en_periodo(self,vinos_filtrados,fecha_desde,fecha_hasta,sommelier):
        puntajes_sommelier_promedio=[]
        puntajes=[]
        
        # Creamos el iterador para los vinos con filtros adicionales
        iterador_vinos = IteradorVinos(vinos_filtrados,filtros=[])
        iterador_vinos.set_filtros({
            "fecha_desde": fecha_desde,
            "fecha_hasta": fecha_hasta,
            "sommelier": sommelier
        })
        iterador_vinos.primero()

        while not iterador_vinos.haTerminado():
            vino = iterador_vinos.actual()  # Obtenemos el vino actual
            if iterador_vinos.cumpleFiltro():  # restringuimos en base a los filtros
                puntaje_resenias = vino.calcular_puntaje_de_sommelier_en_periodo(vino, fecha_desde, fecha_hasta, sommelier)
                puntajes.append(puntaje_resenias)
                puntajes_sommelier_promedio.append(vino.calcular_puntaje_promedio(puntaje_resenias))
            iterador_vinos.siguiente()  # Avanzamos al siguiente vino

        return puntajes, puntajes_sommelier_promedio
    # --------------------------------------------------------------------------------------------------------------------
    
    # Esta función ordena una lista de vinos filtrados por sus puntajes promedio de manera descendente.
    # Agrega los puntajes y puntajes promedio a cada vino en la lista de vinos filtrados.
    # Retorna la lista de vinos ordenada por puntaje promedio en orden descendente.
    def ordenar_vinos(self,vinos_filtrados,puntajes,puntajes_promedio):
        for i, vino in enumerate(vinos_filtrados):
            vino.append(puntajes[i])
            vino.append(puntajes_promedio[i])

        vinos_filtrados_ordenados = sorted(vinos_filtrados, key=lambda x: x[-1], reverse=True)
        return vinos_filtrados_ordenados
    
    def fin_cu(self):
        print("Fin de CU")
        
    def crearIterador(self, elementos):
        if not elementos:
            raise ValueError("La lista de elementos no puede estar vacía.")

        # Verificamos el tipo de elemento para decidir qué iterador crear
        if isinstance(elementos[0], Vino):
            return IteradorVinos(elementos, filtros=[])  # Retorna un iterador de vinos con filtros vacíos
        else:
            raise ValueError("Tipo de elemento no soportado.")
