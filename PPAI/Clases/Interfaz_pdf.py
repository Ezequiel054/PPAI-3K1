from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch

class Interfaz_pdf:
    def __new__(cls):
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self):
        pass

    # Funcion que se encarga de tranformar los datos en PDF
    def exportar_pdf(self,datos):
        pdf_filename = "vinos.pdf"
        doc = SimpleDocTemplate(pdf_filename, pagesize=landscape(letter))
        elements = []

        titulo = Paragraph("<b>10 vinos con mejor calificación de sommeliers</b>", ParagraphStyle(name='Title', fontSize=12))
        elements.append(titulo)
        elements.append(Spacer(1, 0.3 * inch))

        headers_sommelier = ['Nombre Vino', 'Mejor Puntaje', 'Puntaje Promedio', 'Precio', 'Nombre Bodega', 'Región', 'País']
        max_sommelier_scores = max(len(row[5]) for row in datos)
        for i in range(1, max_sommelier_scores + 1):
            headers_sommelier.append(f'Puntaje S{i}')

        headers_variedades = [f'Varietal {i}' for i in range(1, max_sommelier_scores + 1)]

        data_sommelier = [headers_sommelier]
        for row in datos[:10]:
            max_score = max(row[5])
            sommelier_scores = row[5] + [None] * (max_sommelier_scores - len(row[5]))
            wine_data = [row[0], max_score, row[6], row[1], row[2], row[3][0], row[3][1]]
            wine_data.extend(sommelier_scores)
            data_sommelier.append(wine_data)

        table_sommelier = Table(data_sommelier, repeatRows=1)

        data_variedades = [headers_variedades]

        for row in datos[:10]:
            varietals = row[4] + [None] * (max_sommelier_scores - len(row[4]))
            data_variedades.append(varietals)

        table_variedades = Table(data_variedades, repeatRows=1)

        table_style = [('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
                    ('GRID', (0, 0), (-1, -1), 1, colors.white)] 

        data_style = [('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 0), (-1, -1), 6)]

        table_sommelier.setStyle(TableStyle(table_style + data_style))
        table_variedades.setStyle(TableStyle(table_style + data_style))

        table_sommelier.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.beige)]))
        table_variedades.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.beige)]))

        for table in [table_sommelier, table_variedades]:
            for i in range(1, len(data_sommelier)):
                if i % 2 == 0:
                    table.setStyle(TableStyle([('BACKGROUND', (0, i), (-1, i), colors.lightgrey)]))

        elements.append(table_sommelier)
        elements.append(table_variedades)

        return elements
