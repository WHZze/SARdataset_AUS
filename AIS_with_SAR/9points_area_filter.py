# -*- coding: UTF-8 -*-
import arcpy
import os
import fnmatch
import time

#保留在sar影像内的AIS数据点，相当于空间滤波
path = r'F:\WHZ\Zze\SAR_vessel\SAR_AUS\\'
try:
    begin = time.time()
    months = os.listdir(path)[:12]

    #month = 'AIS201912'
    #months = ['AIS201901','AIS201902','AIS201903','AIS201904','AIS201905','AIS201906','AIS201907','AIS201908', 'AIS201909', 'AIS201910', 'AIS201911','AIS201912']
    #months = ['AIS201701']
    for month in months:
        inpath1 = r"F:\WHZ\Zze\SAR_vessel\AUS_2015\\" + 'AIS'+month + '_time_filter'
        #inpath1 = r"F:\WHZ\Zze\SAR_vessel\AUS_2017\\" + month + '_time_filter_100s'
        inpath2 = r"F:\WHZ\Zze\SAR_vessel\SAR_AUS\\" + month
        outpath = r"F:\WHZ\Zze\SAR_vessel\AUS_2015\boatday_areafilter\\" + 'AIS'+month
        #outpath = r"F:\WHZ\Zze\SAR_vessel\AUS_2017\boatday_areafilter\\" + 'AIS'+month + '_100s'
        os.mkdir(outpath)
        print (month + '  is finished!')

        parten='*.shp'
        SAR_filenames=fnmatch.filter(os.listdir(inpath2),parten)


        for SAR_filename in SAR_filenames:
            AIS_filenames = fnmatch.filter(os.listdir(inpath1), parten)
            date = SAR_filename[:-4]
            for AIS_filename in AIS_filenames:
                if AIS_filename.find(SAR_filename) !=-1:
                    if SAR_filename.find(date)!=-1:
                        feature2=inpath2+ '\\' + SAR_filename

                        feature1=inpath1+ '\\' + SAR_filename
                        arcpy.Intersect_analysis([feature1, feature2], outpath+ '\\' + SAR_filename, 'ALL', '', '')
                        print (feature2 + ' ' + feature1)

except arcpy.ExecuteError:
    print arcpy.GetMessages()



end = time.time()
print ('time is %d seconds' %(end-begin))

'''for infile1 in infiles1:
    for infile2 in infiles2:
        if (infile1.find('AIS201909Zone2001')!=-1): 
            print infile1
            feature1 = inpath1 + infile1
            feature2 = inpath2 
            arcpy.Intersect_analysis([feature1, feature2], outpath+infile1, 'ALL', '', '')
            print (feature1+' '+feature2)
            print ('filter:'+infile2)'''




