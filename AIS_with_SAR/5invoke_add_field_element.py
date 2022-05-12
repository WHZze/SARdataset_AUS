# -*- coding:UTF-8 -*-
import datetime
import os #加载os库
import glob
import arcpy #加载arcpy库
import time

#AISs = ['AIS201708','AIS201709','AIS201710','AIS201711']

#for AIS in AISs:
file_dir_BenDi1 = r"F:\WHZ\Zze\SAR_vessel\AUS_2016\\"
#file_dir_BenDi1 = r'F:\WHZ\Zze\SAR_vessel\test\\'
pattern = ".shp"
start=time.time()
filenames = os.listdir(file_dir_BenDi1)
for filename in filenames:
    fileList = [i for i in os.listdir(file_dir_BenDi1 + filename) if i[-4:] == pattern]  # 输出文件为.shp文件

    num = 0
    for file in fileList:
        shpFile = file_dir_BenDi1 + filename + "\\" + file

        arcpy.AddField_management(shpFile, "DAY", "Text", "", "","20")  # 增加一列 "DAY" 的字符串类型的一列属性
        expression = "getDay(!TIMESTAMP!)"  # 必须在字段名称两边添加惊叹号
        codeblock = """def getDay(TIMESTAMP):
            part=TIMESTAMP.split(' ')[0][1:2] 
            if TIMESTAMP.split(' ')[0][1:2]=="/":
                day=TIMESTAMP.split(' ')[0][-4:]+TIMESTAMP.split(' ')[0][-7:-5]+'0'+TIMESTAMP.split(' ')[0][0:1]
            else:
                day = TIMESTAMP.split(' ')[0][-4:] + TIMESTAMP.split(' ')[0][-7:-5] + TIMESTAMP.split(' ')[0][:2]
            return day"""
    # .split() 通过指定分隔符对字符串进行切片
        arcpy.CalculateField_management(shpFile, "DAY", expression, "PYTHON_9.3", codeblock)


        print(file[:-4]+'   is done!')
end=time.time()
print ('time is %d second'%(end-start))