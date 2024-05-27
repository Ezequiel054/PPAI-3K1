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

    def opcion_generar_ranking_vinos(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Bonvino")
        self.root.resizable(False, False)

        self.root.configure(bg="#800020")

        self.cerrar_presionado = False

        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")


        """
        estilo_boton = {
            "bg": "white",       # Fondo blanco
            "fg": "#800020",     # Texto color vino
            "font": mi_tipo_de_letra,
            "relief": "raised",  # Estilo de sombra
        }
        """

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

    def tomar_sel_fecha_desde(self):
        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        Label(self.root, text="Fecha Desde", foreground="black", font=mi_tipo_de_letra).pack(padx=20, pady=25)
        self.cal_desde = DateEntry(self.root, width=45, background="black", foreground="white", bd=2)
        self.cal_desde.pack(pady=25)
        self.cal_desde.configure(state="readonly")
        self.cal_desde.bind("<<DateEntrySelected>>", lambda event: self.validar_periodo())

    def tomar_sel_fecha_hasta(self):
        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        Label(self.root, text="Fecha Hasta", foreground="black", font=mi_tipo_de_letra).pack(padx=20, pady=25)
        self.cal_hasta = DateEntry(self.root, width=45, background="black", foreground="white", bd=2)
        self.cal_hasta.pack(pady=25)
        self.cal_hasta.configure(state="readonly")
        self.cal_hasta.bind("<<DateEntrySelected>>", lambda event: self.validar_periodo())

    def validar_periodo(self):
        fecha_desde = self.cal_desde.get_date()
        fecha_hasta = self.cal_hasta.get_date()

        if fecha_desde >= fecha_hasta:
            self.error_label.config(text="La fecha hasta debe ser mayor que la fecha desde.")
            return

        self.error_label.config(text="Fechas validas ...")
        self.root.quit()
        
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

    def cerrar_press(self):
        self.cerrar_presionado = True
        self.root.quit()

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
# funcion propia del lenguaje para centrar las ventanas       
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry("{}x{}+{}+{}".format(width, height, x, y))

