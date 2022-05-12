# _*_coding:utf-8_*_
# @Time : 2022/1/2 14:37
# @Author : Zze
# @File : BatchProject.py
# @Software : PyCharm
import arcpy
import os
import fnmatch
import time

path = r'F:\WHZ\Zze\NEW\PLAT_1\2017\\'
output = r'F:\WHZ\Zze\NEW\PLAT_2\2017\\'
filenames = fnmatch.filter(os.listdir(path),'*.shp')
prj = r"F:\WHZ\Zze\SAR_vessel\AUS_2017\AIS201701\20170101.prj"
start=time.time()

for filename in filenames:
    isExist = os.path.exists(output+filename)
    if not isExist:
        arcpy.BatchProject_management(path+filename,output,prj)
        #print filename + " has been finished!"

end=time.time()
print ('time is %d second'%(end-start))