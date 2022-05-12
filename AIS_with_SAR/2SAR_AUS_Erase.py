# _*_coding:utf-8_*_
# @Time : 2021/11/14 10:43
# @Author : Zze
# @File : 3SAR_AUS_Erase.py
# @Software : PyCharm
import arcpy
import os
import time
import fnmatch

# sar polygon 擦除澳大利亚部分

file1 = r'F:\WHZ\Zze\SAR_vessel\gadm36_AUS_shp\gadm36_AUS_0.shp'
# file2=r'F:\WHZ\Zze\SAR_2017_boundary_polygon\201701\20170101.shp'
infolder = r'F:\WHZ\Zze\SAR_vessel\SAR_AUS_Intersect\\'
outfolder = r'F:\WHZ\Zze\SAR_vessel\SAR_AUS\\'
begin = time.time()
try:
    foldernames = os.listdir(infolder)[-12:]  # 201701 201702...
    for foldername in foldernames:  # 201701
        os.mkdir(outfolder+foldername)
        print(foldername + '  is made')

        partten = '*.shp'
        filenames = fnmatch.filter(os.listdir(infolder+foldername),partten)
        for filename in filenames:

            isExist = os.path.exists(outfolder + foldername + '\\' + filename)
            if not isExist:
                arcpy.Erase_analysis(infolder+ foldername + '\\'+filename, file1, outfolder+ foldername + '\\'+filename,'')
                print (filename+ '   finished!')

except arcpy.ExecuteError:
       print arcpy.GetMessages()

end = time.time()
print('time is %d seconds ' % (end - begin))