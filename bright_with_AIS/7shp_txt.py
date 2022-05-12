# -*- coding: UTF-8 -*-
import arcpy
import fnmatch
import os



input_shp = r'F:\WHZ\Zze\NEW\PLAT3\2015\\'
#outpath=r"F:\WHZ\Zze\SAR_vessel\AUS_2019\boatday_AIS_result_txt\\"
outpath = r'F:\WHZ\Zze\NEW\result_txt\2015\\'
#txtname='20170804.txt'
path1 = os.listdir(input_shp)
for p1 in path1:
    isExist = os.path.exists(outpath + p1)
    if not isExist:
        os.mkdir(outpath + p1)
        print(p1 + '  is made')
    else:
        continue
    shp_names=fnmatch.filter(os.listdir(input_shp+p1),'*.shp')
    #shp_names = ['merge_shp.shp']
    for shp_name in shp_names:
        rows=arcpy.SearchCursor(input_shp+p1+'\\'+shp_name)
        list=[]     #直接从shp中读取属性信息
        for row in rows:
            id=str(row.FID)
            #craft_id = str(row.CRAFT_ID)
            #basetime=str(row.TIMESTAMP)
            lon=str(row.Lon_1)
            lat=str(row.Lat_1)
            SAR_name=str(row.Name)

            #list.append(id+','+craft_id+','+basetime[-8:]+','+lat+','+lon+','+SAR_name)
            list.append(id + ',' + lat + ',' + lon + ',' + SAR_name)
        if len(list) == 0:
            continue

        list1=[]
        list1.append(list[0])       #装去除冗余后的数据，第一行先加入list1
        list_craft_basetime=[]
        list_craft_basetime.append(list[0].split(',')[1]+','+list[0].split(',')[2])
        #flag=0
        for i in list:
            select=i.split(',')[1]+','+i.split(',')[2]


            #print (select)
            if select in set(list_craft_basetime):
                pass
            else:
                #print (select+'_'+'in!')
                list1.append(i)
                list_craft_basetime.append(select)
        #print (list_mmsi_basetime)
        #print (list1)

        filetxt=open(outpath + p1+'\\'+shp_name[:-4]+'.txt','w')
        for i in list1:
            t = ''
            t = t + i
            # print t
            filetxt.write(t)
            filetxt.write('\n')

        filetxt.close()
        print (shp_name+'  '+'finishied!')

    #print(list)