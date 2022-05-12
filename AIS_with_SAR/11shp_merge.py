# _*_coding:utf-8_*_
# @Time : 2021/11/16 19:37
# @Author : Zze
# @File : 10test.py
# @Software : PyCharm
import os
import fnmatch
import shapefile
import shutil

months = ['AIS201501', 'AIS201502', 'AIS201503', 'AIS201504', 'AIS201505', 'AIS201506', 'AIS201507', 'AIS201508','AIS201509', 'AIS201510', 'AIS201511', 'AIS201512']
#months = ['AIS201701_100s']
outpath = r'F:\WHZ\Zze\SAR_vessel\AUS_2015\boatday_AIS_result_merge\\'
#outpath = r'F:\WHZ\Zze\SAR_vessel\AUS_2017\test_merge\\'
#shp_path = r'F:\WHZ\Zze\SAR_vessel\AUS_2019\boatday_AIS_result\\'
shp_path = r'F:\WHZ\Zze\SAR_vessel\AUS_2015\boatday_AIS_result\\'

for month in months:
    filenames = fnmatch.filter(os.listdir(shp_path+month),'*.shp')
    for filename in filenames:
        sf = shapefile.Reader(shp_path + month + '\\' + filename)
        shapes = sf.shapes()

        if len(shapes) == 0:
            print(filename[:-4]+'  is null!')
        else:
            fs = fnmatch.filter(os.listdir(shp_path+month),filename[:8]+'*')
            for f in fs:
                shutil.copy((shp_path+month+ '\\' + f),outpath)