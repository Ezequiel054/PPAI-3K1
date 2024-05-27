from tkinter import *
from tkinter import messagebox,ttk,simpledialog,font
from datetime import datetime
import csv


class Gestor_ranking_vinos:
    def __new__(cls):
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self):
        pass

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
    
    def calcular_puntaje_de_sommelier_en_periodo(self,vinos_filtrados,fecha_desde,fecha_hasta,sommelier):
        puntajes_sommelier_promedio=[]
        puntajes=[]
        for vino in vinos_filtrados:
            puntaje_resenias=vino.calcular_puntaje_de_sommelier_en_periodo(vino,fecha_desde,fecha_hasta,sommelier)
            puntajes.append(puntaje_resenias)
            puntajes_sommelier_promedio.append(vino.calcular_puntaje_promedio(puntaje_resenias))
        return puntajes,puntajes_sommelier_promedio
    
    def ordenar_vinos(self,vinos_filtrados,puntajes,puntajes_promedio):
        for i, vino in enumerate(vinos_filtrados):
            vino.append(puntajes[i])
            vino.append(puntajes_promedio[i])

        vinos_filtrados_ordenados = sorted(vinos_filtrados, key=lambda x: x[-1], reverse=True)
        return vinos_filtrados_ordenados
    
    def fin_cu(self):
        print("Fin de CU")