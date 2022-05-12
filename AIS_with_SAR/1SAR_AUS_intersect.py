#  -*- coding: UTF-8 -*-
import arcpy
import os
import time
import fnmatch
import datetime

#merge后的sar polygon与AUS边界相交得到澳大利亚的SAR


file1 = r'F:\WHZ\Zze\SAR_vessel\data_scope\scope.shp'
# file2=r'F:\WHZ\Zze\SAR_2017_boundary_polygon\201701\20170101.shp'
infolder = r'F:\WHZ\Zze\SAR_vessel\SAR_polygon\2017\\'
outfolder = r'F:\WHZ\Zze\SAR_vessel\SAR_AUS_Intersect\\'
starttime = datetime.datetime.now()
try:

    #out=r'F:\lab\boat_task\usa_shp\temp1'
    foldernames = os.listdir(infolder)
    #foldernames = ['201901']
    for foldername in foldernames:  # 201701
        os.mkdir(outfolder+foldername)
        print(foldername + '  is made')


        partten='*.shp'
        filenames=fnmatch.filter(os.listdir(infolder+foldername),partten)
        for filename in filenames:

            isExist = os.path.exists(outfolder+ foldername + '\\'+filename)
            if not isExist:
                arcpy.Intersect_analysis([file1,infolder+ foldername + '\\'+filename],outfolder+ foldername + '\\'+filename,'','','')
                #arcpy.Intersect_analysis([file1,file2],out,'','','')
                print (filename+'    finished!')

except arcpy.ExecuteError:
    print arcpy.GetMessages()

endtime = datetime.datetime.now()
print("Time: "+str((endtime - starttime).seconds))