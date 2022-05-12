# _*_coding:utf-8_*_
# @Time : 2021/12/18 18:29
# @Author : Zze
# @File : stationary_ship2.py
# @Software : PyCharm
import arcpy
import fnmatch
import os
import time

year = '2018'
shppath = r'F:\WHZ\Zze\SAR_vessel\stillship\\' + year + '\\'
months = os.listdir(shppath)
begin = time.time()
for month in months:
    filenames = fnmatch.filter(os.listdir(shppath+month),year+'*.shp')

    for filename in filenames:
        mylist = []
        with open(shppath+month+'\\'+filename[-6:-4]+'.txt', 'r') as f:
            list = f.readlines()
            for x in list:
                xx = x.split('\n')[0]
                mylist.append(xx)
        rows = arcpy.UpdateCursor(shppath+month+'\\'+filename)
        for row in rows:
            CRAFT_ID = str(row.CRAFT_ID)
            if CRAFT_ID not in mylist:
                rows.deleteRow(row)
        print filename+'   is done!'
end = time.time()
print('time is %d seconds ' % (end - begin))