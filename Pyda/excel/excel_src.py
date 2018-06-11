##coding=utf-8
import xlrd
import xlwt

'''
  文件的路径很重要，以下方式写路径。
  xlrd 只能读取
  xlwt 只能写

'''
#读取文件路径并转码
file_path = r"/Users/work/Exceldata/user.xlsx"

#file_path = file_path.encode("utf-8")
'''
如果是文件名包含中文使用"decode"进行解码,转换成utf-8
'''
#打开文件，读取数据
data = xlrd.open_workbook(file_path)

#获取sheet数据,根据sheet名字获取
#table = data.sheet_by_name("sheet1")
#打开第一sheet
table = data.sheets()[0]


#获取总的行数
nrows = table.nrows

#获取总的列数
ncols = table.ncols

print(ncols)

for i in range(nrows):
    if i == 0 :
        continue  #如果是第一行就跳过
    ncol_value = table.row_values(i)

    print(ncol_value)