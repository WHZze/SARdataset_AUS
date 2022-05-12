# _*_coding:utf-8_*_
# @Time : 2021/12/11 15:47
# @Author : Zze
# @File : merge_shp.py
# @Software : PyCharm
import arcpy
import fnmatch
import os

shppath = r'F:\WHZ\Zze\SAR_vessel\stillship\2018\\'
outpath = r'F:\WHZ\Zze\SAR_vessel\stillship\2018\\'
months = os.listdir(shppath)
for month in months:
    list_folders = []
    list_files = []
    for file in os.listdir(shppath+month):
        file_path = os.path.join(shppath+month, file)
        if os.path.isdir(file_path):
            list_folders.append(file)
    for AIS in list_folders:
        if len(os.listdir(shppath+month+'\\'+AIS)) != 0:
            shpfiles = fnmatch.filter(os.listdir(shppath+month+'\\'+AIS), '*.shp')
            list0=[]
            for shpfile in shpfiles:
                list0.append(shppath+month+'\\'+AIS+'\\'+ shpfile)
            isExist = os.path.exists(outpath+month+'\\' + 'merge'+AIS[-4:]+'.shp')
            if not isExist:
                arcpy.Merge_management(list0, outpath+month+'\\' + 'merge'+AIS[-4:]+'.shp')
                print 'merge'+AIS[-4:] + " is done!"







