import openpyxl

#打开excel文件
workbook=openpyxl.load_workbook (r"D:\DSUsers\uif46649\ziliao\python\S202 MLC60 Risk Assessment_20230118.xlsx")

#选择要操作的工作表
sheet = workbook['MLC60_65']

#查找指定内容所在的单元格
search_value = 'FS'
for row in sheet.iter_rows():
    for cell in row:
        if cell.value == search_value:
            print(f'"{search_value}" found in cell {cell.coordinate}')