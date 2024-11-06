import sqlite3
import os
import random

from Clases.Entity.Vino import Vino
from Clases.Entity.Varietal import Varietal
from Clases.Entity.Region_vitivinicola import Region_vitivinicola
from Clases.Entity.Provincia import Provincia
from Clases.Entity.Pais import Pais
from Clases.Entity.Resenia import Resenia
from Clases.Entity.Bodega import Bodega

class ConexionDB:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ConexionDB, cls).__new__(cls)
            cls._instance._conexion = None
            cls._instance._cursor = None
            cls._initialize_connection()
        return cls._instance

    @classmethod
    def _initialize_connection(cls):
        try:
            # Asegurarse de que la carpeta 'Datos' exista
            db_path = os.path.join(os.path.dirname(__file__), 'vinos.sqlite3')
            
            # Eliminar la base de datos si existe (opcional)
            if os.path.exists(db_path):
                os.remove(db_path)

            # Conectar a la base de datos
            cls._instance._conexion = sqlite3.connect(db_path)
            cls._instance._cursor = cls._instance._conexion.cursor()
            print("Conexión a la base de datos establecida.")
            
            # Ejecutar el archivo .sql para inicializar la base de datos, si es necesario
            sql_path = os.path.join(os.path.dirname(__file__), 'vinos.sqlite3.sql')
            if os.path.exists(sql_path):
                try:
                    with open(sql_path, 'r') as sql_file:
                        sql_script = sql_file.read()
                    cls._instance._cursor.executescript(sql_script)
                    cls._instance._conexion.commit()
                    print("Script de inicialización ejecutado con éxito.")
                except sqlite3.Error as e:
                    print(f"Error al ejecutar el script SQL: {e}")
                except Exception as ex:
                    print(f"Error inesperado: {ex}")
            else:
                print("Error--El archivo de inicialización SQL no se encontró.")

        except sqlite3.Error as e:
            print(f"Error--No se pudo conectar con la BD: {e}")

    @property
    def conexion(self):
        return self._conexion

    @property
    def cursor(self):
        return self._cursor
    
    def close(self):
        if self._conexion:
            self._conexion.close()
            self._conexion = None
            self._cursor = None
            print("Conexión cerrada.")
    
    def conectar(self):
        try:
            db_path = os.path.join(os.path.dirname(__file__), 'vinos.sqlite3')
            self._conexion = sqlite3.connect(db_path)
            self._cursor = self._conexion.cursor()
            print("Conexión a la base de datos establecida.")
        except sqlite3.Error as e:
            print(f"Error--No se pudo conectar con la BD: {e}")
        
            
    # VINOS
    def consultar_vinos(self):
        lista_vinos = []
        try:
            # Asegúrate de que la conexión esté inicializada
            if self._conexion is None:
                self._initialize_connection()
            
            # Comprobar si el cursor está disponible
            if self._cursor is not None:
                self._cursor.execute("SELECT * FROM Vino")  # Cambia esto si necesitas columnas específicas
                vinos_data = self._cursor.fetchall()  # Obtener todos los resultados

                # Procesar cada fila de resultados
                for vino_data in vinos_data:
                    # Asumiendo que tu constructor de Vino acepta estos parámetros
                    vino = Vino(*vino_data)  # Ajusta esto según el número y tipo de parámetros del constructor
                    lista_vinos.append(vino)  # Agregar el objeto vino a la lista

            else:
                print("Error: El cursor no está inicializado.")
        
        except sqlite3.Error as e:
            print(f"Error al consultar los vinos: {e}")
        
        return lista_vinos

    def insertar_pais(self, pais):
        self.cursor.execute('INSERT INTO Pais (nombre) VALUES (?)', (pais.nombre,))
        self.conexion.commit()
        return self.cursor.lastrowid

    def insertar_provincia(self, provincia):
        pais_id = self.insertar_pais(provincia.pais)  # Insertar país y obtener su ID
        self.cursor.execute('INSERT INTO Provincia (nombre, pais_id) VALUES (?, ?)', (provincia.nombre, pais_id))
        self.conexion.commit()
        return self.cursor.lastrowid

    def insertar_region(self, region):
        provincia_id = self.insertar_provincia(region.provincia)  # Insertar provincia y obtener su ID
        self.cursor.execute('INSERT INTO Region_vitivinicola (nombre, descripcion, provincia_id) VALUES (?, ?, ?)',
                            (region.nombre, region.descripcion, provincia_id))
        self.conexion.commit()
        return self.cursor.lastrowid

    def insertar_varietal(self, varietal):
        self.cursor.execute('INSERT INTO Varietal (descripcion, composicion) VALUES (?, ?)', 
                            (varietal.descripcion, varietal.porcentajeComposicion))
        self.conexion.commit()
        return self.cursor.lastrowid

    def insertar_bodega(self, bodega):
        region_id = self.insertar_region(bodega.region)  # Insertar región y obtener su ID
        self.cursor.execute('INSERT INTO Bodega (nombre, ubicacion_coordenadas, descripcion, fecha_ultima_actualizacion, historia, periodo_actualizacion, region_id) VALUES (?, ?, ?, ?, ?, ?, ?)',
                            (bodega.nombre, bodega.coordenadas_ubicacion, bodega.descripcion, bodega.fecha_ultima_actualizacion, bodega.historia, bodega.periodo_actualizacion, region_id))
        self.conexion.commit()
        return self.cursor.lastrowid

    def insertar_vino(self, vino):
        bodega_id = self.insertar_bodega(vino.bodega)  # Insertar bodega y obtener su ID
        self.cursor.execute('INSERT INTO Vino (aniada, fecha_actualizacion, imagen_etiqueta, nombre, nota_de_cata, precio_ars, bodega_id) VALUES (?, ?, ?, ?, ?, ?, ?)',
                            (vino.aniada, vino.fecha_actualizacion, vino.imagen_etiqueta, vino.nombre, vino.nota_de_cata_bodega, vino.precio_ars, bodega_id))
        self.conexion.commit()
        vino_id = self.cursor.lastrowid  # Obtener ID del vino insertado
        
        # Insertar varietales asociados
        for varietal in vino.varietales:
            varietal_id = self.insertar_varietal(varietal)
            self.cursor.execute('INSERT INTO Vino_Varietal (vino_id, varietal_id) VALUES (?, ?)', (vino_id, varietal_id))
        self.conexion.commit()
        
        return vino_id

    def insertar_resenia(self, resenia):
        vino_id = self.insertar_vino(resenia.vino)  # Insertar vino y obtener su ID
        self.cursor.execute('INSERT INTO Resenia (comentario, es_premium, fecha, puntaje, vino_id) VALUES (?, ?, ?, ?, ?)',
                            (resenia.comentario, resenia.es_premium, resenia.fecha, resenia.puntaje, vino_id))
        self.conexion.commit()




def generar_varietales():
    descripciones_varietales = [
        "Notas intensas de frutos rojos.",
        "Notas cítricas y tropicales.",
        "Notas intensas de frutas negras."
    ]

    porcentajes_composicion_varietales = [
        "75% Cabernet Sauvignon, 20% Merlot, 5% Petit Verdot",
        "60% Malbec, 30% Syrah, 10% Cabernet Franc",
        "100% Chardonnay"
    ]

    varietales = []
    for i in range(3):
        varietal = Varietal(descripciones_varietales[i], porcentajes_composicion_varietales[i])
        varietales.append(varietal)

    return varietales

def carga_datos():
    # Conectar a la base de datos
    conexion = ConexionDB()
    conexion.conectar()  # Asegurarse de que la conexión esté activa

    # Creación de los objetos necesarios previos
    varietales = generar_varietales()

    # Crear regiones y provincias
    pais = "Argentina"  # Definir un país

    conexion.cursor.execute('INSERT INTO Pais (nombre) VALUES (?)', (pais,))
    pais_id = conexion.cursor.lastrowid  # Obtener ID del país insertado

    # Crear provincias inicialmente con el ID de provincia como None
    provincias = [
        Provincia("Mendoza", None, pais),
        Provincia("San Juan", None, pais),
        Provincia("La Rioja", None, pais)
    ]

    # Insertar provincias en la base de datos y asignarles el ID
    for provincia in provincias:
        conexion.cursor.execute('INSERT INTO Provincia (nombre, pais_id) VALUES (?, ?)', 
                                (provincia.nombre, pais_id))
        provincia.id = conexion.cursor.lastrowid  # Asignar el ID a la provincia

    # Crear regiones y asociarlas con las provincias usando sus IDs
    regiones = [
        Region_vitivinicola("Mendoza", "Descripción de Mendoza", provincias[0].id),
        Region_vitivinicola("San Juan", "Descripción de San Juan", provincias[1].id),
        Region_vitivinicola("La Rioja", "Descripción de La Rioja", provincias[2].id)
    ]

    # Insertar regiones en la base de datos usando los IDs de las provincias
    for region in regiones:
        conexion.cursor.execute('INSERT INTO Region_vitivinicola (nombre, descripcion, provincia_id) VALUES (?, ?, ?)', 
                                (region.nombre, region.descripcion, region.provincia))



    # Lista de nombres de bodegas (deberás definirla previamente)
    nombres_bodegas = [
        "Bodega Santa Rita", "Bodega San Telmo", "Bodegas Torres",
        "Bodega Norton", "Bodega Zuccardi", "Bodega Trapiche"
    ]
    historia_bodega = "Fundada en 1998 por la familia González, Bodega Valle Escondido ha crecido desde sus humildes comienzos hasta convertirse en una reconocida bodega en la región. Nuestro enfoque en la calidad y la pasión por el vino nos ha llevado a ganar numerosos premios y reconocimientos a lo largo de los años."

    # Lista de nombres de vinos
    nombres_vinos = [
        "Cabernet Sauvignon", "Merlot", "Pinot Noir", "Chardonnay", "Sauvignon Blanc",
        "Syrah", "Malbec", "Zinfandel", "Riesling", "Gewürztraminer",
        "Tempranillo", "Sangiovese", "Barbera", "Nebbiolo", "Grenache",
        "Chenin Blanc", "Viognier", "Carmenere", "Petit Verdot", "Albariño"
    ]

    # Generar 20 vinos con datos aleatorios
    vinos_generados = []
    for i in range(20):
        # Detalles del vino
        añada = 2020
        fecha_actualizacion_vino = "12-05-2024"
        imagen_etiqueta = "url_imagen"
        nombre_vino = nombres_vinos[i]
        nota_de_cata_bodega = "Este vino es el resultado de una cuidadosa selección de uvas maduras y una crianza en barricas de roble francés durante 12 meses. Presenta aromas intensos a frutos negros, notas de vainilla y toques de tabaco. En boca es redondo y equilibrado, con taninos suaves y un final largo y persistente."
        precio_ars = random.randint(15200, 54000)

        # Seleccionar aleatoriamente una región y provincia
        region = random.choice(regiones)
        provincia = region.provincia
        
        # Crear el objeto Bodega
        nombre_bodega=random.choice(nombres_bodegas)
        coordenadas_ubicacion_bodega = "40.7128° N, 74.0060° W"  # Ajusta según sea necesario
        descripcion_bodega = "Descripción de " + nombre_bodega
        fecha_ultima_actualizacion_bodega = "12-05-2024"
        periodo_actualizacion_bodega = "anual"

        # Insertar la bodega en la base de datos
        conexion.cursor.execute('INSERT INTO Bodega (ubicacion_coordenadas, descripcion, fecha_ultima_actualizacion, historia, nombre, periodo_actualizacion, region_id) VALUES (?, ?, ?, ?, ?, ?, ?)',
                                (coordenadas_ubicacion_bodega, descripcion_bodega, fecha_ultima_actualizacion_bodega, historia_bodega, nombre_bodega, periodo_actualizacion_bodega, nombre_bodega))
        
        bodega_id = conexion.cursor.lastrowid  # Obtener ID de la bodega insertada

        # Generar una cantidad aleatoria de varietales para este vino (de 1 a 3)
        num_varietales = random.randint(1, 3)
        varietales_vino = random.sample(varietales, num_varietales)

        # Crear el vino
        vino = Vino(añada, fecha_actualizacion_vino, imagen_etiqueta, nombre_vino, nota_de_cata_bodega, precio_ars, bodega_id, varietales_vino, None)

        # Generar un número aleatorio de reseñas para este vino (de 1 a 3)
        num_resenias = random.randint(1, 3)
        resenias_vino = []
        for _ in range(num_resenias):
            # Crear una reseña
            comentario_resenia = "¡Este vino es simplemente asombroso! Tiene una complejidad excepcional y un equilibrio perfecto entre fruta y roble."
            es_premium_resenia = random.choice([True, False])
            fecha_resenia = "12-05-2024"
            puntaje_resenia = round(random.uniform(1, 5), 2)
            resenia = Resenia(comentario_resenia, es_premium_resenia, fecha_resenia, puntaje_resenia, vino)
            resenias_vino.append(resenia)

        # Asignar las reseñas al vino
        vino.resenias = resenias_vino

        # Insertar vino y sus reseñas en la base de datos
        conexion.cursor.execute('INSERT INTO Vino (aniada, fecha_actualizacion, imagen_etiqueta, nombre, nota_de_cata, precio_ars, bodega_id) VALUES (?, ?, ?, ?, ?, ?, ?)',
                                (vino.aniada, vino.fecha_actualizacion, vino.imagen_etiqueta, vino.nombre, vino.nota_de_cata_bodega, vino.precio_ars, nombre_bodega))
        
        vino_id = conexion.cursor.lastrowid  # Obtener ID del vino insertado
        
        # Insertar varietales asociados
        for varietal in vino.varietal:
            varietal_id = conexion.cursor.execute('INSERT INTO Varietal (descripcion, composicion) VALUES (?, ?)', 
                                                  (varietal.descripcion, varietal.porcentajeComposicion)).lastrowid
            conexion.cursor.execute('INSERT INTO Vino_Varietal (vino_id, varietal_id) VALUES (?, ?)', (vino_id, varietal_id))
        
        # Insertar reseñas
        for resenia in vino.resenias:
            conexion.cursor.execute('INSERT INTO Resenia (comentario, es_premium, fecha, puntaje, vino_id) VALUES (?, ?, ?, ?, ?)',
                                    (resenia.comentario, resenia.es_premium, resenia.fecha_resenia, resenia.puntaje, vino_id))

        # Agregar el vino a la lista de vinos generados
        vinos_generados.append(vino)

    # Confirmar cambios y cerrar conexión
    conexion.conexion.commit()
    conexion.conexion.close()
    return vinos_generados

# Ejecutar la función y obtener los vinos generados
vinos = carga_datos()