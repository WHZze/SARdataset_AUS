# -*- coding: UTF-8 -*-
import arcpy
#import array.da
import os
import fnmatch
import time
import datetime

#保留在对应的sar影像成像时间内的AIS数据点，相当于第二次时间滤波

shp_path=r'F:\WHZ\Zze\SAR_vessel\AUS_2015\boatday_areafilter\\'
months = ['AIS201501', 'AIS201502', 'AIS201503', 'AIS201504', 'AIS201505', 'AIS201506', 'AIS201507', 'AIS201508','AIS201509', 'AIS201510', 'AIS201511', 'AIS201512']
#months = ['AIS201701_100s']
out_path=r'F:\WHZ\Zze\SAR_vessel\AUS_2015\boatday_AIS_result\\'
partten='*.shp'
begin = time.time()

for month in months:

    new_foldername=out_path+month  # F:\WHZ\Zze\SAR_vessel\AUS_2017\boatday_AIS_result\AIS201701
    os.mkdir(new_foldername)
    print ('new folder is made:')

    filenames=fnmatch.filter(os.listdir(shp_path+month),partten)            #AIS20170101.shp
    for filename in filenames:

        arcpy.MakeFeatureLayer_management(shp_path+month+'\\'+filename,  "wlh")         #临时创建
        arcpy.CopyFeatures_management("wlh",new_foldername+'\\'+filename)     #复制未筛选的shp
        rows=arcpy.UpdateCursor(new_foldername+'\\'+filename)
        arcpy.Delete_management("wlh")
        #theFields=arcpy.ListFields(shp_file)      #读取shp的所有字段名
        #print (theFields)
        #theFields=['FID','Shape *','FID_AIS201','Field1','MMSI','BaseDateTi','LAT','LON','SOG','COG',\
        #           'Heading','VesselName','IMO','CallSign','VesselType','Status','Length','Width',\
        #           'Draft','Cargo','FID_201709','FID_USA','Id','FID_USA','Id_1','Name','TIME','TIME1']
        #rows=arcpy.da.UpdateCursor(out_path+'\\'+'wlh',theFields)
        #arcpy.CopyFeatures_management(row,out_path+'wlh')
        for row in rows:
            delta=datetime.timedelta(seconds=0)
            Time0 = str(row.TIMESTAMP)
            if len(Time0) > 10:
                AIS_time = Time0[-8:]
                AIS_time = datetime.datetime.strptime(AIS_time, '%H:%M:%S')
            else:
                Time0 = Time0 + ' 00:00:00'
                AIS_time = Time0[-8:]
                AIS_time = datetime.datetime.strptime(AIS_time, '%H:%M:%S')
            Time=str(row.TIME)
            Time1=str(row.TIME1)
            Time=Time[0:2]+':'+Time[2:4]+':'+Time[4:6]
            Time1=Time1[0:2]+':'+Time1[2:4]+':'+Time1[4:6]
            Time=datetime.datetime.strptime(Time,'%H:%M:%S')
            Time1=datetime.datetime.strptime(Time1,'%H:%M:%S')

            #AIS_time=AIS_time-datetime.timedelta(seconds=35)
            #print Time
            #print Time1
            #print AIS_time
            delta1=AIS_time-Time
            delta2=Time1-AIS_time
            if not (delta1>=delta and delta2>=delta):
                rows.deleteRow(row)

        print (filename[:-4]+' is finished!')




end = time.time()
print('time is %d seconds ' % (end - begin))