import csv

from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    with open(csv_path,'r',encoding="utf-8") as f:
         read = csv.reader(f)
         for row in read:
              ws.append(row)
        
    for column in ws.columns:
        column_letter = column[0].column_letter  # Получаем букву колонки (A, B, C...)
        max_length = 8  # Минимальная ширина
        
        for cell in column:
            if cell.value:
                # Ищем самую длинную строку в колонке
                max_length = max(max_length, len(str(cell.value)))
        
        # Устанавливаем ширину колонки
        ws.column_dimensions[column_letter].width = max_length + 2
    
    wb.save(xlsx_path)
          
csv_to_xlsx('src\data\lab_05\samples\people.csv','src\data\lab_05\out\people.xlsx')