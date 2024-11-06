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
    _conexion = None
    _cursor = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ConexionDB, cls).__new__(cls)
            cls._initialize_connection()
        return cls._instance

    @classmethod
    def _initialize_connection(cls):
        """Initialize the database connection."""
        try:
            db_path = 'vinos.db'
            cls._instance._conexion = sqlite3.connect(db_path)
            cls._instance._cursor = cls._instance._conexion.cursor()
            print("Conexión a la base de datos establecida.")
        except sqlite3.Error as e:
            print(f"Error--No se pudo conectar con la BD: {e}")

    @classmethod
    def get_instance(cls):
        """Obtain a single instance of the database connection."""
        if cls._instance is None:
            cls._instance = ConexionDB()
            cls._initialize_connection()
        return cls._instance

    @property
    def conexion(self):
        return self._conexion

    @property
    def cursor(self):
        return self._cursor
    
    def get_connection(self):
        """Obtiene la conexión a la base de datos."""
        return self._conexion
    
    def close(self):
        if self._conexion:
            self._conexion.close()
            self._conexion = None
            self._cursor = None
            print("Conexión cerrada.")
    
    def conectar(self):
        try:
            self._conexion = sqlite3.connect('vinos.db')
            self._cursor = self._conexion.cursor()
            print("Conexión establecida exitosamente")
        except sqlite3.Error as e:
            print(f"Error--No se pudo conectar con la BD: {e}")
        
   
    def crear_tablas(self):
        cursor = self.conexion.cursor()
        
        # Creación de tablas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Pais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Provincia (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                pais_id INTEGER,
                FOREIGN KEY(pais_id) REFERENCES Pais(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Region_vitivinicola (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                descripcion TEXT,
                provincia_id INTEGER,
                FOREIGN KEY(provincia_id) REFERENCES Provincia(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Bodega (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                descripcion TEXT,
                historia TEXT,
                coordenadas TEXT,
                region_id INTEGER,
                fecha_ultima_actualizacion TEXT,  
                periodo_actualizacion TEXT, 
                FOREIGN KEY(region_id) REFERENCES Region_vitivinicola(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Varietal (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descripcion TEXT,
                composicion TEXT
            )
        ''')
        
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS Vino_Varietal (
                vino_id INTEGER,
                varietal_id INTEGER,
                FOREIGN KEY(vino_id) REFERENCES Vino(id),
                FOREIGN KEY(varietal_id) REFERENCES Varietal(id),
                PRIMARY KEY(vino_id, varietal_id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Vino (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                aniada INTEGER,
                fecha_actualizacion TEXT,
                imagen_etiqueta TEXT,
                nota_de_cata_bodega TEXT,
                precio_ars REAL,
                bodega_id INTEGER,
                FOREIGN KEY(bodega_id) REFERENCES Bodega(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Resenia (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                comentario TEXT,
                es_premium BOOLEAN,
                fecha TEXT,
                puntaje REAL,
                vino_id INTEGER,
                FOREIGN KEY(vino_id) REFERENCES Vino(id)
            )
        ''')

        # Commit y cerrar
        self.get_connection().commit()
    
    # Funciones auxiliares para insertar o reutilizar entidades
    def obtener_o_insertar_pais(self, nombre):
        self.cursor.execute("SELECT id FROM Pais WHERE nombre = ?", (nombre,))
        pais = self.cursor.fetchone()
        if pais:
            return pais[0]
        self.cursor.execute("INSERT INTO Pais (nombre) VALUES (?)", (nombre,))
        return self.cursor.lastrowid

    def obtener_o_insertar_provincia(self, nombre, pais_id):
        self.cursor.execute("SELECT id FROM Provincia WHERE nombre = ? AND pais_id = ?", (nombre, pais_id))
        provincia = self.cursor.fetchone()
        if provincia:
            return provincia[0]
        self.cursor.execute("INSERT INTO Provincia (nombre, pais_id) VALUES (?, ?)", (nombre, pais_id))
        return self.cursor.lastrowid

    def obtener_o_insertar_region(self, nombre, descripcion, provincia_id):
        self.cursor.execute("SELECT id FROM Region_vitivinicola WHERE nombre = ? AND provincia_id = ?", (nombre, provincia_id))
        region = self.cursor.fetchone()
        if region:
            return region[0]
        self.cursor.execute("INSERT INTO Region_vitivinicola (nombre, descripcion, provincia_id) VALUES (?, ?, ?)", (nombre, descripcion, provincia_id))
        return self.cursor.lastrowid

    def obtener_o_insertar_bodega(self, nombre, descripcion, historia, coordenadas, region_id, fecha_ultima_actualizacion, periodo_actualizacion):
        self.cursor.execute("SELECT id FROM Bodega WHERE nombre = ? AND region_id = ?", (nombre, region_id))
        bodega = self.cursor.fetchone()
        if bodega:
            return bodega[0]
        
        # Inserta los datos de la bodega incluyendo las nuevas columnas
        self.cursor.execute("""
            INSERT INTO Bodega (nombre, descripcion, historia, coordenadas, region_id, fecha_ultima_actualizacion, periodo_actualizacion) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (nombre, descripcion, historia, coordenadas, region_id, fecha_ultima_actualizacion, periodo_actualizacion))
        
        return self.cursor.lastrowid

    def obtener_o_insertar_varietal(self, descripcion, composicion):
        self.cursor.execute("SELECT id FROM Varietal WHERE descripcion = ? AND composicion = ?", (descripcion, composicion))
        varietal = self.cursor.fetchone()
        if varietal:
            return varietal[0]
        self.cursor.execute("INSERT INTO Varietal (descripcion, composicion) VALUES (?, ?)", (descripcion, composicion))
        return self.cursor.lastrowid

    def insertar_datos(self, vinos):
        cursor = self.conexion.cursor()
        
        # Insertar los datos en las tablas
        for vino in vinos:
            
            # Insertar o reutilizar Pais
            pais_id = self.obtener_o_insertar_pais(vino.bodega.region.provincia.pais.nombre)
            
            # Insertar o reutilizar Provincia
            provincia_id = self.obtener_o_insertar_provincia(vino.bodega.region.provincia.nombre, pais_id)
            
            # Insertar o reutilizar Region
            region_id = self.obtener_o_insertar_region(vino.bodega.region.nombre, vino.bodega.region.descripcion, provincia_id)
            
            # Insertar o reutilizar Bodega con las nuevas columnas
            fecha_ultima_actualizacion = vino.bodega.fecha_ultima_actualizacion
            periodo_actualizacion = vino.bodega.periodo_actualizacion
            
            bodega_id = self.obtener_o_insertar_bodega(vino.bodega.nombre, vino.bodega.descripcion, vino.bodega.historia, 
                                                        vino.bodega.coordenas_ubicacion, region_id, fecha_ultima_actualizacion, periodo_actualizacion)
            
            # Insertar Vino con las nuevas columnas
            cursor.execute("""
                INSERT INTO Vino (nombre, aniada, fecha_actualizacion, imagen_etiqueta, nota_de_cata_bodega, precio_ars, bodega_id)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (vino.nombre, vino.aniada, vino.fecha_actualizacion, vino.imagen_etiqueta, vino.nota_de_cata_bodega, vino.precio_ars, bodega_id))
            
            vino_id = cursor.lastrowid
            
            # Insertar Varietales
            for varietal in vino.varietal:
                varietal_id = self.obtener_o_insertar_varietal(varietal.descripcion, varietal.porcentajeComposicion)
                cursor.execute("INSERT INTO Vino_Varietal (vino_id, varietal_id) VALUES (?, ?)", (vino_id, varietal_id))
            
            # Insertar Reseñas
            for resenia in vino.resenia:
                cursor.execute("""
                    INSERT INTO Resenia (comentario, es_premium, fecha, puntaje, vino_id) 
                    VALUES (?, ?, ?, ?, ?)
                """, (resenia.comentario, resenia.es_premium, resenia.fecha_resenia, resenia.puntaje, vino_id))
        
        self.get_connection().commit()
