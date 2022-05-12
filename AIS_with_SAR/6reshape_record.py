# _*_coding:utf-8_*_
# @Time : 2021/11/17 22:11
# @Author : Zze
# @File : 8reshape_record.py
# @Software : PyCharm

import datetime
import arcpy
import time
import fnmatch
import os

begin = time.time()
shp_path = r'F:\WHZ\Zze\SAR_vessel\AUS_2016\\'
#shp_path = r'F:\WHZ\Zze\SAR_vessel\test\\'
months = os.listdir(shp_path)[:4]
for month in months:
    fileList = [i for i in os.listdir(shp_path + month) if i[-4:] == '.shp']  # 提取shp文件
#shpname = r'F:\WHZ\Zze\SAR_vessel\AUS_2017\AIS201712\\AIS201712.shp'
    for file in fileList:
        rows = arcpy.UpdateCursor(shp_path + month + '\\' + file)
        for row in rows:
            Time = str(row.TIMESTAMP)
            if Time[-2:] == 'PM':
                if Time[-11] == ' ':
                    a = int(Time[-10]) + 12
                    b = str(a)
                    Time = Time[:-10] + b + Time[-9:]
                elif Time[-11:-9] == '12':
                    Time = Time
                else:
                    a = int(Time[-11:-9]) + 12
                    b = str(a)
                    Time = Time[:-11] + b + Time[-9:]
            elif Time[-2:] == 'AM':
                if Time[-11] == ' ':
                    Time = Time[:-10] + '0' + Time[-10:]
                elif Time[-11:-9] == '12':
                    Time = Time[:-11] + '00' + Time[-9:]
                else:
                    Time = Time
            Time = Time[:-3]
            row.TIMESTAMP = Time
            rows.updateRow(row)
        print (file[-13:] + '  finished!')

end = time.time()
print('time is %d seconds ' % (end - begin))
