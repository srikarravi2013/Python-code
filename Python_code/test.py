from openpyxl import Workbook, load_workbook

book = load_workbook('C:/Users/srika/Desktop/Python code/Book.xlsx')

sheet = book.active

print(sheet['A2'].value)

book.save('C:/Users/srika/Desktop/Python code/Book.xlsx')
