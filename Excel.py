'''import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet("managerdata")
ws = wb.add_sheet("rawdata")
ws.write(1,1,"vinaykumar")
wb.save("/root/Desktop/MyPythonPrograms/mynewworkbook.xls")'''


import csv
import time
f = open('/root/Desktop/MyPythonPrograms/Mydata.csv','r')
reader = csv.reader(f)
for row in reader:
	print(row)
	time.sleep(1)
f.close()


