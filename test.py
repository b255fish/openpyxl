import openpyxl
import os

os.chdir(r'.')
print(os.getcwd())
print(os.listdir())

file = os.listdir()[0]
print(file)

f = open (file,'r',encoding='utf-8')
lines = f.readlines()
for line in lines:
	print(line)
f.close()

print(lines)

wb = openpyxl.Workbook()

sheet = wb.active
sheet.append(lines)
wb.save(r'test.xlsx')