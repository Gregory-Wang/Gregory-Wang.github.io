import mysql.connector
import xlrd
conn = mysql.connector.connect(
    user='root', 
    password='whh990166423', 
    host='localhost', 
    database='frenchtb')

# 输入表格行数量/表格文件名
page = 151
file_name = "table 6"


cur = conn.cursor()
l = list()
loc = (f"G:\\SystemTemp\\桌面\\术语库表\\{file_name}.xls")
a = xlrd.open_workbook(loc)
sheet = a.sheet_by_index(0)
sheet.cell_value(0, 0)
for i in range(1,page):
    l.append(tuple(sheet.row_values(i)))

q = "insert into ftb_term(chinese,french,similar,source,definition,example,cata,tag) values(%s,%s,%s,%s,%s,%s,%s,%s)"
cur.executemany(q, l)
conn.commit()
conn.close()