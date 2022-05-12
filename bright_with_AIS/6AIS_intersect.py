# _*_coding:utf-8_*_
# @Time : 2022/1/5 13:22
# @Author : Zze
# @File : AIS_intersect.py
# @Software : PyCharm
import arcpy
import os
import fnmatch
import time

path = r'F:\WHZ\Zze\NEW\PLAT2\2015\\'

AIS = r'F:\WHZ\Zze\SAR_vessel\AUS_2015\boatday_areafilter\\'
outpath = r'F:\WHZ\Zze\NEW\PLAT3\2015\\'
start1 = time.time()
foldernames = os.listdir(path) #201901,201902...
for foldername in foldernames:
    path1 = os.listdir(path+foldername) #20190101,20190102...
    files = fnmatch.filter(os.listdir(AIS+'AIS'+foldername),'*.shp')



    isExist = os.path.exists(outpath+foldername)
    if not isExist:
        os.mkdir(outpath+foldername)
        print(foldername + '  is made')
    else:
        print(foldername + ' is already exist!')
        continue

    for p1 in path1:
        filenames = fnmatch.filter(os.listdir(path+foldername+'\\'+p1),'*.shp')
        for filename in filenames:
            name = str(filename)[:-4]
            name = name.upper()
            for file1 in files:
                rows = arcpy.SearchCursor(AIS+'AIS'+foldername+'\\'+file1)
                for row in rows:
                    Name = str(row.Name)
                    if Name == name:
                        isExist = os.path.exists(outpath+file1[:6]+'\\'+filename)
                        if not isExist:
                            arcpy.Intersect_analysis([AIS+'AIS'+foldername+'\\'+file1, path+foldername+'\\'+p1+'\\'+filename],
                                                     outpath+file1[:6]+'\\'+filename, '', '', '')
                            # arcpy.Intersect_analysis([file1,file2],out,'','','')
                            if arcpy.GetCount_management(outpath+file1[:6]+'\\'+filename)[0] == "0":
                                arcpy.Delete_management(outpath+file1[:6]+'\\'+filename)
                                #print (filename+  '   is none!')
                            else:
                                print (filename + '    finished!')

end1=time.time()
print ('time is %d second'%(end1-start1))
