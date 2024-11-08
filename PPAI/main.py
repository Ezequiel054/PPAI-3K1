from tkinter import *
from Clases.Boundary.Pantalla_ranking_vinos import *
from Clases.Control.Gestor_ranking_vinos import *  
from Clases.Boundary.Interfaz_excel import *
from Datos.datos import *
from Clases.Boundary.Interfaz_pdf import *


# funcion principal que contiene toda la logica
def main():
    gestor_ranking_vinos = Gestor_ranking_vinos()
    pantalla_ranking_vinos = Pantalla_ranking_vinos()
    
    opcion_generar_ranking_vinos=pantalla_ranking_vinos.opcion_generar_ranking_vinos()
    pantalla_ranking_vinos.habilitar_pantalla()
    gestor_ranking_vinos.opcion_generar_ranking_vinos()
    vinos = gestor_ranking_vinos._vinos
    


    if opcion_generar_ranking_vinos == False:
        fechas=pantalla_ranking_vinos.solicitar_sel_fecha_desde_y_hasta()
        if fechas != True:
            gestor_ranking_vinos.tomar_sel_fecha_desde_y_hasta(fechas[0],fechas[1])
            resenia=pantalla_ranking_vinos.solicitar_sel_tipo_resenia()
            if resenia != True:
                gestor_ranking_vinos.tomar_sel_tipo_resenia(resenia)
                tipo_visualizacion=pantalla_ranking_vinos.solicitar_sel_tipo_visualizacion()
                if tipo_visualizacion!= True:
                    gestor_ranking_vinos.tomar_sel_tipo_visualizacion(tipo_visualizacion)
                    confirmacion=pantalla_ranking_vinos.solicitar_confirmacion_gen_reporte()
                    if confirmacion:
                        vinos_con_resenia_en_periodo=gestor_ranking_vinos.buscar_vinos_con_resenias_en_periodo(vinos,fechas[0],fechas[1],resenia)
                        if vinos_con_resenia_en_periodo[0]:
                            puntajes=gestor_ranking_vinos.calcular_puntaje_de_sommelier_en_periodo(vinos_con_resenia_en_periodo[1],fechas[0],fechas[1],resenia)
                            vinos_ordenados=gestor_ranking_vinos.ordenar_vinos(vinos_con_resenia_en_periodo[0],puntajes[0],puntajes[1])
                            if tipo_visualizacion=="Excel":
                                interfaz_excel=Interfaz_excel()
                                datos_excel=interfaz_excel.exportar_excel(vinos_ordenados)
                                if pantalla_ranking_vinos.confirmar_exportacion("Excel"):
                                    datos_excel.save("Ranking.xlsx")
                                    messagebox.showinfo("Información", "Excel creado con exito.")
                            elif tipo_visualizacion=="PDF":
                                interfaz_pdf=Interfaz_pdf()
                                datos_pdf=interfaz_pdf.exportar_pdf(vinos_ordenados)
                                if pantalla_ranking_vinos.confirmar_exportacion("PDF"):
                                        doc = SimpleDocTemplate("vinos.pdf", pagesize=landscape(letter))
                                        doc.build(datos_pdf)
                                        messagebox.showinfo("Información", "PDF creado con exito.")
                            else:
                                pantalla_ranking_vinos.mostrar_ranking_por_pantalla(vinos_ordenados)
                                               
    gestor_ranking_vinos.fin_cu()
         

if __name__ == '__main__':
    main()
