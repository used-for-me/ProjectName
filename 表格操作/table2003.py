# 操作Excel2003 或者更低
from xlwt import Workbook, Alignment, Borders, XFStyle, Formula
import xlrd

book = Workbook()
sheet1 = book.add_sheet('first sheet')
a1 = Alignment()
a1.horz = Alignment.HORZ_CENTER
a1.vert = Alignment.HORZ_CENTER
borders = Borders()
borders.bottom = Borders.THICK
style = XFStyle()
style.alignment = a1
style.borders = borders
row = sheet1.row(0)
row.write(0, 'test', style=style)
row = sheet1.row(1)
for i in range(5):
    row.write(i, i, style=style)
row.write(5, Formula('SUM(A2:E2)'), style=style)
book.save('./test2003.xls')

book = xlrd.open_workbook('./test2003.xls')
sheet1 = book.sheet_by_name('first sheet')
row = sheet1.row(0)
print(row[0].value)
# 读不到公式，无解
print(sheet1.row(1)[5].value)
# print(sheet1.cell(1, 5).value)
