-- Crear tablas
BEGIN TRANSACTION;

CREATE TABLE Pais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);

CREATE TABLE Provincia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    pais_id INTEGER,
    FOREIGN KEY (pais_id) REFERENCES Pais(id)
);

CREATE TABLE Region_vitivinicola (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    provincia_id INTEGER,
    FOREIGN KEY (provincia_id) REFERENCES Provincia(id)
);

CREATE TABLE Varietal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT,
    composicion TEXT
);

CREATE TABLE Bodega (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    ubicacion_coordenadas TEXT,
    descripcion TEXT,
    fecha_ultima_actualizacion DATE,
    historia TEXT,
    periodo_actualizacion TEXT,
    region_id INTEGER,
    FOREIGN KEY (region_id) REFERENCES Region_vitivinicola(id)
);

CREATE TABLE Vino (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aniada INTEGER,
    fecha_actualizacion DATE,
    imagen_etiqueta TEXT,
    nombre TEXT,
    nota_de_cata TEXT,
    precio_ars INTEGER,
    bodega_id INTEGER,
    FOREIGN KEY (bodega_id) REFERENCES Bodega(id)
);

CREATE TABLE Resenia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comentario TEXT,
    es_premium BOOLEAN,
    fecha DATE,
    puntaje DECIMAL(3,2),
    vino_id INTEGER,
    FOREIGN KEY (vino_id) REFERENCES Vino(id)
);

CREATE TABLE Vino_Varietal (
    vino_id INTEGER,
    varietal_id INTEGER,
    PRIMARY KEY (vino_id, varietal_id),
    FOREIGN KEY (vino_id) REFERENCES Vino(id),
    FOREIGN KEY (varietal_id) REFERENCES Varietal(id)
);

COMMIT;

