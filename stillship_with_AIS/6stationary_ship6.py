# _*_coding:utf-8_*_
# @Time : 2021/12/25 20:31
# @Author : Zze
# @File : stationary_ship6.py
# @Software : PyCharm
import arcpy
import os
import fnmatch
import math
from datetime import datetime
import numpy as np

shppath = r'F:\WHZ\Zze\SAR_vessel\stillship\2018\\'
months = os.listdir(shppath)[8:9]

for month in months:
    list_folders = []
    list_files = []
    for file in os.listdir(shppath+month):
        file_path = os.path.join(shppath+month, file)
        if os.path.isdir(file_path):
            list_folders.append(file)
    for AIS in list_folders:
        print '========='+AIS+'========='
        filenames = fnmatch.filter(os.listdir(shppath+month+'\\'+AIS), '*.shp')
        for filename in filenames:

            rows = arcpy.UpdateCursor(shppath+month+'\\'+AIS+'\\'+filename)
            list1 = []
            for row in rows:
                TIMESTAMP = str(row.TIMESTAMP)
                Time = str(row.TIME)
                Time1 = str(row.TIME1)
                if len(TIMESTAMP) > 10:
                    AIS_time = TIMESTAMP[-8:-6] + TIMESTAMP[-5:-3] + TIMESTAMP[-2:]
                else:
                    AIS_time = '000000'
                '''
                midtime1 = int(np.mean([int(Time[0:2]), int(Time1[0:2])]))
                midtime1 = str(midtime1)
                if len(midtime1) == 1:
                    midtime1 = '0'+midtime1
                midtime2 = int(np.mean([int(Time[2:4]), int(Time1[2:4])]))
                midtime2 = str(midtime2)
                if len(midtime2) == 1:
                    midtime2 = '0'+midtime2
                midtime3 = int(np.mean([int(Time[4:6]), int(Time1[4:6])]))
                midtime3 = str(midtime3)
                if len(midtime3) == 1:
                    midtime3 = '0'+midtime3
                '''
                #a=datetime.now()
                midtime1 = Time[0:2]+':'+Time[2:4]+':'+Time[4:6]
                midtime1 = datetime.strptime(midtime1,"%H:%M:%S")
                midtime2 = Time1[0:2] + ':' + Time1[2:4] + ':' + Time1[4:6]
                midtime2 = datetime.strptime(midtime2, "%H:%M:%S")
                midtime3 = (midtime2-midtime1) / 2
                midtime = str(midtime1+midtime3)
                midtime = int(midtime[11:13]+midtime[14:16]+midtime[17:19])
                AIS_time = int(AIS_time)
                Difference0 = midtime - AIS_time
                Difference = math.fabs(Difference0)
                list1.append(Difference)

            #print list1
            minn = min(list1)
            #print minn
            row1s = arcpy.UpdateCursor(shppath+month+'\\'+AIS+'\\'+filename)
            for row1 in row1s:
                TIMESTAMP = str(row1.TIMESTAMP)
                Time = str(row1.TIME)
                Time1 = str(row1.TIME1)
                if len(TIMESTAMP) > 10:
                    AIS_time = TIMESTAMP[-8:-6] + TIMESTAMP[-5:-3] + TIMESTAMP[-2:]
                else:
                    AIS_time = '000000'
                midtime1 = Time[0:2] + ':' + Time[2:4] + ':' + Time[4:6]
                midtime1 = datetime.strptime(midtime1, "%H:%M:%S")
                midtime2 = Time1[0:2] + ':' + Time1[2:4] + ':' + Time1[4:6]
                midtime2 = datetime.strptime(midtime2, "%H:%M:%S")
                midtime3 = (midtime2 - midtime1) / 2
                midtime = str(midtime1 + midtime3)
                midtime = int(midtime[11:13] + midtime[14:16] + midtime[17:19])
                AIS_time = int(AIS_time)
                Difference0 = midtime - AIS_time
                Difference = math.fabs(Difference0)
                if Difference > minn:
                    row1s.deleteRow(row1)
                    #print row1.FID

            print filename +  '   done!'









