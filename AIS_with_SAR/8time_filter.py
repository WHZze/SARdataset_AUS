# _*_coding:utf-8_*_
# @Time : 2021/11/14 19:53
# @Author : Zze
# @File : 6time_filter.py
# @Software : PyCharm
import fnmatch
import arcpy
import os
import time
import datetime
from interval import Interval

shp_path = r'F:\WHZ\Zze\SAR_vessel\AUS_2015\\'
months = ['AIS201501','AIS201502','AIS201503','AIS201504','AIS201505','AIS201506','AIS201507','AIS201508','AIS201509','AIS201510','AIS201511','AIS201512']
#months = os.listdir(shp_path)
#months = ['AIS201701']
out_path = r'F:\WHZ\Zze\SAR_vessel\AUS_2015\\'


begin = time.time()

for month in months:

    new_foldername = out_path+month+'_time_filter'

    isExist = os.path.exists(new_foldername)
    if not isExist:
        os.mkdir(new_foldername)
        print ('new folder is made: ' + month + '_time_filter')
    else:

        print(new_foldername + ' is already exist!')
        continue

    filenames = fnmatch.filter(os.listdir(shp_path+month),'*.shp')
    for filename in filenames:
        txtname = os.path.splitext(filename)[0]
        results = []
        txt_path = r'F:\WHZ\Zze\SAR_vessel\SAR_Time_better_txt\\' + month[3:]
        isTrue = os.path.exists(txt_path+ '\\' +txtname+'.txt')
        if not isTrue:
            print(txtname+'  does not exist!')
            continue
        else:

            with open(txt_path+ '\\' +txtname+'.txt', 'r') as f:
                for line in f:
                    results.append(line.strip('\n').split(','))

            arcpy.MakeFeatureLayer_management(shp_path+month+'\\'+filename ,  "wlh")
            arcpy.CopyFeatures_management("wlh", new_foldername+'\\'+filename)
            rows=arcpy.UpdateCursor(new_foldername+'\\'+filename)
            arcpy.Delete_management("wlh")
            #print rows
            list = []
            for row in rows:
                #delta = datetime.timedelta(seconds=0)
                Time = str(row.TIMESTAMP)
                #Time = Time+':00'
                FID = str(row.FID)
                if len(Time) > 10:
                    AIS_Time = Time[-8:]
                    AIS_Time = datetime.datetime.strptime(AIS_Time, '%H:%M:%S')
                else:
                    Time = Time + ' 00:00:00'
                    AIS_Time = Time[-8:]
                    AIS_Time = datetime.datetime.strptime(AIS_Time, '%H:%M:%S')

                for result in results:
                    t1 = datetime.datetime.strptime(result[0], '%H:%M:%S')
                    t2 = datetime.datetime.strptime(result[1], '%H:%M:%S')
                    time_interval = Interval(t1, t2)


                    if  (AIS_Time in time_interval):
                        #print "the {} row is wanted".format(row.FID)
                        list.append(FID)
                if FID not in list:
                    rows.deleteRow(row)

            print (filename[:-4] + '  is finished!')

end = time.time()
print ('time is %d seconds' %(end-begin))