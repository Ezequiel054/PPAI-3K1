from Clases.Vino import *
from Clases.Varietal import *
from Clases.Resenia import *
from Clases.Bodega import *
from Clases.Region_vitivinicola import *
from Clases.Provincia import *
from Clases.Pais import *
import random

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
    # Creación de los objetos necesarios previos
    # Variedad de uva
    varietales = generar_varietales()

    # Región
    descripciones_regiones = [
        "La región de Valle de Uco es conocida por sus excelentes condiciones para el cultivo de la vid, con altitudes que favorecen la maduración lenta de las uvas y suelos de gran calidad.",
        "Es predominantemente semidesértica, y su viticultura depende del riego de los ríos San Juan y Jachal",
        "Se ha asociado recientemente con vinos de calidad para exportación, cuando hasta principios del siglo XXI, solo se cultivaban uvas de mesa y pasas por estos lares"
    ]

    nombres_regiones = ["Valle Dorado", "Montañas del Vino", "Llanuras Aromáticas"]
    regiones = []
    for i in range(3):
        region = Region_vitivinicola(descripciones_regiones[i], nombres_regiones[i], None)
        regiones.append(region)

    # Provincia
    nombre_provincias = ["Mendoza", "San Juan", "La Rioja"]
    provincias = []
    for i in range(3):
        provincia = Provincia(nombre_provincias[i], regiones[i], None)
        regiones[i].provincia = provincia  # Asociar provincia a la región
        provincias.append(provincia)

    # País
    nombre_paises = ["Argentina","Argentina","Argentina"]
    paises = []
    for i in range(3):
        pais = Pais(nombre_paises[i], [provincias[i]])
        provincias[i].pais = pais  # Asociar país a la provincia
        paises.append(pais)

    # Bodega
    coordenadas_ubicacion_bodega = "40.7128° N, 74.0060° W"
    descripcion_bodega = "Bodega Valle Escondido es un proyecto familiar ubicado en el corazón de la región vinícola, dedicado a la producción de vinos de alta calidad. Nuestros viñedos se extienden sobre suelos pedregosos que otorgan a nuestros vinos su carácter distintivo y expresivo."
    fecha_ultima_actualizacion_bodega = "12-05-2024"
    historia_bodega = "Fundada en 1998 por la familia González, Bodega Valle Escondido ha crecido desde sus humildes comienzos hasta convertirse en una reconocida bodega en la región. Nuestro enfoque en la calidad y la pasión por el vino nos ha llevado a ganar numerosos premios y reconocimientos a lo largo de los años."
    nombres_bodegas = [
        "Bodega Santa Rita",
        "Bodega San Telmo",
        "Bodegas Torres"
    ]
    periodo_actualizacion_bodega = "anual"

    # Crear una lista para almacenar los vinos
    vinos_generados = []
    
    nombres_vinos = [
        "Cabernet Sauvignon",
        "Merlot",
        "Pinot Noir",
        "Chardonnay",
        "Sauvignon Blanc",
        "Syrah",
        "Malbec",
        "Zinfandel",
        "Riesling",
        "Gewürztraminer",
        "Tempranillo",
        "Sangiovese",
        "Barbera",
        "Nebbiolo",
        "Grenache",
        "Chenin Blanc",
        "Viognier",
        "Carmenere",
        "Petit Verdot",
        "Albariño"
    ]
    # Generar 20 vinos con datos aleatorios
    for i in range(20):
        # Detalles del vino
        añada = 2020
        fecha_actualizacion_vino = "12-05-2024"
        imagen_etiqueta = "url_imagen"
        nombre_vino = nombres_vinos[i]
        nota_de_cata_bodega = "Este vino es el resultado de una cuidadosa selección de uvas maduras y una crianza en barricas de roble francés durante 12 meses. Presenta aromas intensos a frutos negros, notas de vainilla y toques de tabaco. En boca es redondo y equilibrado, con taninos suaves y un final largo y persistente."
        precio_ars = random.randint(15200,54000)

        # Seleccionar un nombre de bodega aleatorio
        nombre_bodega = random.choice(nombres_bodegas)

        # Seleccionar aleatoriamente una región, provincia y país
        region = random.choice(regiones)
        provincia = region.provincia
        pais = provincia.pais

        # Crear el objeto Bodega
        bodega = Bodega(coordenadas_ubicacion_bodega, descripcion_bodega, fecha_ultima_actualizacion_bodega, historia_bodega, nombre_bodega, periodo_actualizacion_bodega, region)

        # Generar una cantidad aleatoria de varietales para este vino (de 1 a 3)
        num_varietales = random.randint(1, 3)
        varietales_vino = random.sample(varietales, num_varietales)

        # Crear el vino
        vino = Vino(añada, fecha_actualizacion_vino, imagen_etiqueta, nombre_vino, nota_de_cata_bodega, precio_ars, bodega, varietales_vino, None)

        # Generar un número aleatorio de reseñas para este vino (de 1 a 3)
        num_resenias = random.randint(1, 3)
        resenias_vino = []
        for _ in range(num_resenias):
            # Crear una reseña
            comentario_resenia = "¡Este vino es simplemente asombroso! Tiene una complejidad excepcional y un equilibrio perfecto entre fruta y roble."
            prem=[True,False]
            es_premium_resenia = random.choice(prem)
            fecha_resenia = "12-05-2024"
            puntaje_resenia = round(random.uniform(1, 5),2)
            resenia = Resenia(comentario_resenia, es_premium_resenia, fecha_resenia, puntaje_resenia, vino)
            resenias_vino.append(resenia)

        # Asignar las reseñas al vino
        vino.resenias = resenias_vino

        # Agregar el vino a la lista de vinos generados
        vinos_generados.append(vino)

    return vinos_generados

# Ejecutar la función y obtener los vinos generados
vinos = carga_datos()



