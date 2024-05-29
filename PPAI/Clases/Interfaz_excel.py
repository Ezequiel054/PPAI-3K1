from openpyxl import Workbook

class Interfaz_excel:
    def __new__(cls):
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self):
        pass

    # Funcion que se encarga de tranformar los datos en Excel
    def exportar_excel(self,datos):
        wb = Workbook()
        ws = wb.active

        headers_sommelier = ['Nombre Vino', 'Mejor Puntaje de Sommelier', 'Puntaje Promedio de Sommelier', 'Precio', 'Nombre Bodega', 'Región', 'País']
        max_sommelier_scores = max(len(row[5]) for row in datos)
        for i in range(1, max_sommelier_scores + 1):
            headers_sommelier.append(f'Puntaje Sommelier {i}')

        headers_variedades = []
        for i in range(1, max_sommelier_scores + 1):
            headers_variedades.append(f'Varietal {i}')

        headers = headers_sommelier + headers_variedades
        ws.append(headers)

        for row in datos[:10]:
            max_score = max(row[5])
            sommelier_scores = row[5] + [None] * (max_sommelier_scores - len(row[5]))
            varietals = row[4] + [None] * (max_sommelier_scores - len(row[4]))
            wine_data = [row[0], max_score, row[6], str(row[1]), row[2], row[3][0], row[3][1]]
            wine_data.extend(sommelier_scores)
            wine_data.extend(varietals)
            ws.append(wine_data)
                        
        for col in ws.columns:
            max_length = 0
            column = col[0].column_letter 
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            adjusted_width = (max_length + 2)
            ws.column_dimensions[column].width = adjusted_width

        return wb 
