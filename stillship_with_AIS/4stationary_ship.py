# _*_coding:utf-8_*_
# @Time : 2021/12/22 10:49
# @Author : Zze
# @File : stationary_ship3.py
# @Software : PyCharm
import arcpy
import os
import fnmatch
import time

shppath = r'F:\WHZ\Zze\SAR_vessel\stillship\2018\\'
sarpath = r'F:\WHZ\Zze\SAR_vessel\SAR_AUS\\'
months = os.listdir(shppath)[8:9]
for month in months:

    filenames = fnmatch.filter(os.listdir(shppath+month),'*.shp')

    for filename in filenames:
        if not os.path.exists(sarpath+month+'\\'+filename):
            continue
        isExist = os.path.exists(shppath+month+'\\'+'AIS'+filename)
        if not isExist:
            arcpy.Intersect_analysis([shppath+month+'\\'+filename, sarpath+month+'\\'+filename],shppath+month+'\\'+'AIS'+filename, '', '', '')
            arcpy.Delete_management(shppath+month+'\\'+filename)
            print ('AIS'+filename + '    finished!')


#shppath = r'F:\WHZ\Zze\SAR_vessel\AUS_2017\stillship_0\\'
'''
filenames = fnmatch.filter(os.listdir(shppath),'*.shp')

for filename in filenames:
    if filename[:3] == 'AIS':
        list1 = []
        list2 = []
        rows = arcpy.SearchCursor(shppath+filename)
        for row in rows:
            ID = str(row.CRAFT_ID)
            list1.append(ID)
            list2 = list(set(list1))
        print len(list2)'''