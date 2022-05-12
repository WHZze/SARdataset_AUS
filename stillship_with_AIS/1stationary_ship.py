# _*_coding:utf-8_*_
# @Time : 2021/12/18 16:06
# @Author : Zze
# @File : stationary_ship.py
# @Software : PyCharm
import arcpy
import os
import fnmatch
import time

months = ['AIS201801','AIS201802','AIS201803','AIS201804','AIS201805','AIS201806','AIS201807','AIS201808', 'AIS201809', 'AIS201810', 'AIS201811','AIS201812']
begin = time.time()
months = months
for month in months:
    shppath = r'F:\WHZ\Zze\SAR_vessel\AUS_2018\\' + month + '\\'
    outpath = r'F:\WHZ\Zze\SAR_vessel\stillship\2018\\'+month[3:] + '\\'
    isExists1 = os.path.exists(outpath)
    if not isExists1:
        os.mkdir(outpath)
        print outpath+'  is made!'
    filenames = fnmatch.filter(os.listdir(shppath),'*.shp')

    for filename in filenames:

        arcpy.MakeFeatureLayer_management(shppath+filename, "wlh")
        arcpy.CopyFeatures_management("wlh", outpath+filename)
        rows = arcpy.UpdateCursor(outpath+filename)
        arcpy.Delete_management("wlh")
        list0 = []
        for row in rows:
            speed = float(row.SPEED)
            FID = str(row.FID)

            if speed == 0:
                list0.append(FID)

            if FID not in list0:
                rows.deleteRow(row)
        print filename + '     is done!'

end = time.time()
print('time is %d seconds ' % (end - begin))
print '========done!========'
