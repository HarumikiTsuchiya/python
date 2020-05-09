import openpyxl
"""
EXCWLデータ練習
"""

wb = openpyxl.load_workbook("./Book1.xlsx")

for sheet in wb :
    for raw in sheet:
        for cell in raw:
            print(cell.value)


