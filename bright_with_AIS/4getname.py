# _*_coding:utf-8_*_
# @Time : 2021/12/31 17:06
# @Author : Zze
# @File : getname.py
# @Software : PyCharm
import arcpy
import os
import fnmatch
import time


#path = r'F:\WHZ\Zze\NEW\PLAT_MOSAIC_SUM_REGION_POLYGON_SELECT_CANDIDATE\\'
path = r'F:\WHZ\Zze\NEW\PLAT_2\2017\\'
filenames = fnmatch.filter(os.listdir(path),'*.shp')

start1=time.time()
for filename in filenames:
    start = time.time()
    fieldList = arcpy.ListFields(path+filename)

    lens = len(fieldList)
    if lens == 5:
        ''' 
        for field in fieldList:
            if field.name == "NAME" or field.name == "Lon" or field.name == "Lat" or field.name == "DAY" or field.name == "TIME" or field.name == "TIME1":
                # Execute DeleteField
                arcpy.DeleteField_management(path + filename, "NAME")
                arcpy.DeleteField_management(path + filename, "Lon")
                arcpy.DeleteField_management(path + filename, "Lat")
                arcpy.DeleteField_management(path + filename, "DAY")
                arcpy.DeleteField_management(path + filename, "TIME")
                arcpy.DeleteField_management(path + filename, "TIME1")
                print " FeatureLayer's  Field already delete!"
                break'''

        arcpy.AddField_management(path+filename,"NAME","TEXT","","","70")
        arcpy.AddField_management(path+filename, "Lon", "double", 9, 6)
        arcpy.AddField_management(path+filename, "Lat", "double", 9, 6)
        arcpy.AddField_management(path+filename,"DAY","TEXT","","","20")
        arcpy.AddField_management(path + filename, "TIME", "TEXT", "", "", "10")
        arcpy.AddField_management(path + filename, "TIME1", "TEXT", "", "", "10")
        expression1 = "!SHAPE.Centroid.X!"
        expression2 = "!SHAPE.Centroid.Y!"
        str = filename.encode("utf-8")  # 将Unicode类型转化为string型数据
        str = str.split('.')[0]  # 将str进行切割，将"文件名.shp"中的".shp"去掉
        str = str.upper()
        arcpy.CalculateField_management(path+filename,"NAME","\""+str +"\"","PYTHON_9.3")
        arcpy.CalculateField_management(path+filename, "Lon", expression1, "PYTHON_9.3")
        arcpy.CalculateField_management(path+filename, "Lat", expression2, "PYTHON_9.3")
        arcpy.CalculateField_management(path+filename,"DAY","\""+str[17:25] +"\"","PYTHON_9.3")
        arcpy.CalculateField_management(path+filename,"TIME","\""+str[26:32] +"\"","PYTHON_9.3")
        arcpy.CalculateField_management(path+filename,"TIME1","\""+str[42:48] +"\"","PYTHON_9.3")
        end = time.time()
        print filename + "  NAME field has been finished!" + ' time is %d second'%(end-start)

end1=time.time()
print ('time is %d second'%(end1-start1))