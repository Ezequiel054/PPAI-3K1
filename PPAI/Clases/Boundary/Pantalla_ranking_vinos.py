from tkinter import *
from tkinter import messagebox,ttk,simpledialog,font
from datetime import datetime
from tkcalendar import Calendar, DateEntry
from tkinter.ttk import Combobox

class Pantalla_ranking_vinos():
    def __new__(cls):
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self):
        pass
    
    # Esta función crea una ventana de interfaz gráfica con un botón para generar un reporte de ranking de vinos.
    def opcion_generar_ranking_vinos(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Bonvino")
        self.root.resizable(False, False)

        self.root.configure(bg="#800020")

        self.cerrar_presionado = False

        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.boton = Button(self.root, text="Generar Reporte Ranking", font=mi_tipo_de_letra, command=self.root.quit)
        self.boton.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.boton.config(height=3, width=25) 
        self.boton.place(relx=0.5, rely=0.5, anchor="center")

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        center_window(self.root)
        self.root.mainloop()

        if self.cerrar_presionado:
            return True
        else:return False

    def habilitar_pantalla(self):
        pass
    
    # Esta función crea una ventana de interfaz gráfica para seleccionar un rango de fechas "Desde" y "Hasta".
    # Permite al usuario seleccionar las fechas, validar el periodo, y confirmar su selección.
    # Retorna True si se presiona el botón de cerrar, o las fechas seleccionadas en formato "dd-mm-yyyy" si se confirma la selección
    def solicitar_sel_fecha_desde_y_hasta(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Bonvino")

        self.root.configure(bg="#800020")

        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.tomar_sel_fecha_desde()

        self.tomar_sel_fecha_hasta()

        self.boton = Button(self.root, text="Enviar", command=self.validar_periodo, font=mi_tipo_de_letra, fg="black")
        self.boton.config(height=3, width=25)  
        self.boton.pack(pady=40)

        self.error_label = Label(self.root, text="", foreground="black", background="#800020", font=mi_tipo_de_letra)
        self.error_label.config(height=5)
        self.error_label.pack(pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        center_window(self.root)
        self.root.mainloop()

        self.root.mainloop()

        if self.cerrar_presionado:
            return True
        else:
            return self.cal_desde.get_date().strftime("%d-%m-%Y"),self.cal_hasta.get_date().strftime("%d-%m-%Y")

    # Esta función crea una ventana de interfaz gráfica para seleccionar un rango de fechas "Desde" y "Hasta".
    # Permite al usuario seleccionar las fechas, validar el periodo, y confirmar su selección.
    # Retorna True si se presiona el botón de cerrar, o las fechas seleccionadas en formato "dd-mm-yyyy" si se confirma la selección
    def tomar_sel_fecha_desde(self):
        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        Label(self.root, text="Fecha Desde", foreground="black", font=mi_tipo_de_letra).pack(padx=20, pady=25)
        self.cal_desde = DateEntry(self.root, width=45, background="black", foreground="white", bd=2)
        self.cal_desde.pack(pady=25)
        self.cal_desde.configure(state="readonly")
        self.cal_desde.bind("<<DateEntrySelected>>", lambda event: self.validar_periodo())

    # Esta función crea y configura un selector de fecha "Hasta" en la ventana principal.
    def tomar_sel_fecha_hasta(self):
        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        Label(self.root, text="Fecha Hasta", foreground="black", font=mi_tipo_de_letra).pack(padx=20, pady=25)
        self.cal_hasta = DateEntry(self.root, width=45, background="black", foreground="white", bd=2)
        self.cal_hasta.pack(pady=25)
        self.cal_hasta.configure(state="readonly")
        self.cal_hasta.bind("<<DateEntrySelected>>", lambda event: self.validar_periodo())

    # Esta función valida que la fecha "Desde" no sea mayor o igual que la fecha "Hasta".
    # Muestra un mensaje de error si la validación falla y cierra la ventana si las fechas son válidas.
    def validar_periodo(self):
        fecha_desde = self.cal_desde.get_date()
        fecha_hasta = self.cal_hasta.get_date()

        if fecha_desde >= fecha_hasta:
            self.error_label.config(text="La fecha hasta debe ser mayor que la fecha desde.")
            return

        self.error_label.config(text="Fechas validas ...")
        self.root.quit()
    
    # Esta función crea una ventana de interfaz gráfica para seleccionar el tipo de reseña.
    def solicitar_sel_tipo_resenia(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Bonvino")
        self.root.configure(bg="#800020")

        self.tomar_tipo_resenia()

        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.boton = Button(self.root, text="Enviar", command=self.root.quit, font=mi_tipo_de_letra, fg="black")
        self.boton.config(height=3, width=25)  
        self.boton.place(relx=0.5, rely=0.9, anchor='center')

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        center_window(self.root)
        self.root.mainloop()

        if self.cerrar_presionado:
            return True
        else:
            return self.tipo_resenia.get()

    # Esta función crea y configura un combobox para seleccionar el tipo de reseña en la ventana principal.
    def tomar_tipo_resenia(self):
        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        # Crear y posicionar la etiqueta
        label = Label(self.root, text="Seleccionar Tipo de Reseña", foreground="black", font=mi_tipo_de_letra)
        label.place(relx=0.5, rely=0.3, anchor='center')  # Posicionar en el centro de la ventana

        # Crear y posicionar el combo box
        self.tipo_resenia = StringVar(self.root)
        self.tipo_resenia.set("Sommelier")  # Valor por defecto
        opciones_resenia = ["Reseñas normales", "Sommelier", "Amigos"]
        self.combo_resenia = Combobox(self.root, textvariable=self.tipo_resenia, values=opciones_resenia)
        self.combo_resenia.place(relx=0.5, rely=0.4, anchor='center')  # Posicionar en el centro de la ventana
        self.combo_resenia.configure(state="readonly")

    # Esta función crea una ventana de interfaz gráfica para seleccionar el tipo de visualización.
    def solicitar_sel_tipo_visualizacion(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Bonvino")

        self.root.configure(bg="#800020")

        self.tomar_tipo_visualizacion()

        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.boton = Button(self.root, text="Enviar", command=self.root.quit, font=mi_tipo_de_letra, fg="black")
        self.boton.config(height=3, width=25)  
        self.boton.place(relx=0.5, rely=0.9, anchor='center')

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        center_window(self.root)
        self.root.mainloop()

        if self.cerrar_presionado:
            return True
        else:
            return self.tipo_visualizacion.get()

    # Esta función crea y configura un combobox para seleccionar el tipo de visualización en la ventana principal.
    def tomar_tipo_visualizacion(self):
        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        label = Label(self.root, text="Seleccionar Tipo de Visualizacion", foreground="black", font=mi_tipo_de_letra)
        label.place(relx=0.5, rely=0.3, anchor='center')

        self.tipo_visualizacion = StringVar(self.root)
        self.tipo_visualizacion.set("Excel")
        opciones_visualizacion = ["Excel", "PDF", "Pantalla"]
        self.combo_visualizacion = Combobox(self.root, textvariable=self.tipo_visualizacion, values=opciones_visualizacion)
        self.combo_visualizacion.place(relx=0.5, rely=0.4, anchor='center')
        self.combo_visualizacion.configure(state="readonly")

    # Funcion para tomar el cierre de la ventana
    def cerrar_press(self):
        self.cerrar_presionado = True
        self.root.quit()

    # Esta función crea una ventana para solicitar la confirmación del usuario antes de generar el reporte de ranking.
    def solicitar_confirmacion_gen_reporte(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Bonvino")
        self.root.configure(bg="#800020")

        self.confirmado = False

        self.label_confirmacion = Label(self.root, text="¿Desea generar el reporte Ranking?", font=("Arial", 16), bg="#800020", fg="white")
        self.label_confirmacion.place(relx=0.5, rely=0.4, anchor="center")

        self.tomar_confirmacion_gen_reporte()

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        center_window(self.root)
        self.root.mainloop()

        if self.confirmado:
            return True
        else:
            return False

    # funcion propia del boton   
    def confirmar(self):
        self.confirmado = True
        self.root.quit()

    # funcion propia del boton 
    def cancelar(self):
        self.confirmado = False
        self.root.quit()

    # Esta función configura los botones de confirmación y cancelación en la ventana de confirmación para generar el reporte de ranking.
    def tomar_confirmacion_gen_reporte(self):
        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.boton_confirmar = Button(self.root, text="Confirmar", command=self.confirmar, font=mi_tipo_de_letra, fg="black")
        self.boton_confirmar.config(height=3, width=12)
        self.boton_confirmar.place(relx=0.35, rely=0.6, anchor="center")

        self.boton_cancelar = Button(self.root, text="Cancelar", command=self.cancelar, font=mi_tipo_de_letra, fg="black")
        self.boton_cancelar.config(height=3, width=12)
        self.boton_cancelar.place(relx=0.65, rely=0.6, anchor="center")


    def confirmar_exportacion(self,tipo):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Bonvino")
        self.root.configure(bg="#800020")

        self.confirmado = False

        texto=f'¿Desea confirmar la exportacion en {tipo}?'
        self.label_confirmacion = Label(self.root, text=texto, font=("Arial", 16), bg="#800020", fg="white")
        self.label_confirmacion.place(relx=0.5, rely=0.4, anchor="center")

        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.boton_confirmar = Button(self.root, text="Confirmar", command=self.confirmar, font=mi_tipo_de_letra, fg="black")
        self.boton_confirmar.config(height=3, width=12)
        self.boton_confirmar.place(relx=0.35, rely=0.6, anchor="center")

        self.boton_cancelar = Button(self.root, text="Cancelar", command=self.cancelar, font=mi_tipo_de_letra, fg="black")
        self.boton_cancelar.config(height=3, width=12)
        self.boton_cancelar.place(relx=0.65, rely=0.6, anchor="center")

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        center_window(self.root)
        self.root.mainloop()

        if self.confirmado:
            return True
        else:
            return False

    def mostrar_ranking_por_pantalla(self, datos):
        ventana = Tk()
        ventana.title("Tabla de Vinos")

        encabezados_sommelier = ['Nombre Vino', 'Mejor Puntaje de Sommelier', 'Puntaje Promedio de Sommelier', 'Precio', 'Nombre Bodega', 'Región', 'País']
        max_puntajes_sommelier = max(len(fila[5]) for fila in datos)
        for i in range(1, max_puntajes_sommelier + 1):
            encabezados_sommelier.append(f'Puntaje Sommelier {i}')

        encabezados_variedades = []
        for i in range(1, max_puntajes_sommelier + 1):
            encabezados_variedades.append(f'Varietal {i}')

        encabezados = encabezados_sommelier + encabezados_variedades

        tabla = ttk.Treeview(ventana, columns=encabezados, show="headings")
        for encabezado in encabezados:
            ancho_columna = 150  
            tabla.heading(encabezado, text=encabezado, anchor=CENTER)
            tabla.column(encabezado, width=ancho_columna, anchor=CENTER)

        for fila_datos in datos[:10]:
            max_puntaje = max(fila_datos[5])
            puntajes_sommelier = fila_datos[5]
            if isinstance(puntajes_sommelier, str):
                puntajes_sommelier = [int(puntaje) if puntaje.isdigit() else "" for puntaje in puntajes_sommelier.split(",")]
            puntajes_sommelier += [""] * (max_puntajes_sommelier - len(puntajes_sommelier))

            variedades = fila_datos[4] if isinstance(fila_datos[4], list) else [fila_datos[4]]
            variedades += [""] * (max_puntajes_sommelier - len(variedades))
            if len(fila_datos) >= 7:
                if isinstance(fila_datos[3], (list, tuple)):
                    datos_vino = [fila_datos[0], max_puntaje, fila_datos[6], str(fila_datos[1]), fila_datos[2], fila_datos[3][0], fila_datos[3][1]]
                    datos_vino.extend(puntajes_sommelier)
                    datos_vino.extend(variedades)
                    tabla.insert("", "end", values=datos_vino)
                else:
                    pass
            else:
                print("Error: El número de elementos en la fila no es suficiente.")

        for encabezado in encabezados:
            tabla.heading(encabezado, text=encabezado, command=lambda _encabezado=encabezado: treeview_sort_column(tabla, _encabezado, False))
        
        tabla.pack(expand=True, fill=BOTH)
        
        boton_cerrar = Button(ventana, text="Cerrar Todo", command=ventana.quit)
        boton_cerrar.pack(pady=10)

        center_window(ventana)
        ventana.mainloop()


# funcion propia del lenguaje para centrar las ventanas       
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry("{}x{}+{}+{}".format(width, height, x, y))

# Función propia del lenguaje para ordenar las columnas de mostrar por pantalla el ranking.
def treeview_sort_column(tabla, col, reverse):
    lista = [(tabla.set(k, col), k) for k in tabla.get_children('')]
    lista.sort(reverse=reverse)

    for index, (valor, k) in enumerate(lista):
        tabla.move(k, '', index)

    tabla.heading(col, command=lambda: treeview_sort_column(tabla, col, not reverse))