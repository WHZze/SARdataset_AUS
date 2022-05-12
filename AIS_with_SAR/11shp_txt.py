# -*- coding: UTF-8 -*-
import arcpy
import fnmatch
import os


input_shp = r"F:\WHZ\Zze\SAR_vessel\AUS_2015\boatday_AIS_result_merge\\"
outpath=r"F:\WHZ\Zze\SAR_vessel\AUS_2015\boatday_AIS_result_txt\\"
#txtname='20170804.txt'
shp_names=fnmatch.filter(os.listdir(input_shp),'*.shp')

for shp_name in shp_names:
    rows=arcpy.SearchCursor(input_shp+shp_name)
    list=[]     #直接从shp中读取属性信息
    for row in rows:
        id=str(row.FID)
        craft_id = str(row.CRAFT_ID)
        basetime=str(row.TIMESTAMP)
        lon=str(row.LON)
        lat=str(row.LAT)
        SAR_name=str(row.Name)

        list.append(id+','+craft_id+','+basetime[-8:]+','+lat+','+lon+','+SAR_name)


    list1=[]
    list1.append(list[0])       #装去除冗余后的数据，第一行先加入list1
    list_craft_basetime=[]
    list_craft_basetime.append(list[0].split(',')[1]+','+list[0].split(',')[2])
    #flag=0
    for i in list:
        select=i.split(',')[1]+','+i.split(',')[2]


        #print (select)
        if  select in set(list_craft_basetime):
            pass
        else:
            #print (select+'_'+'in!')
            list1.append(i)
            list_craft_basetime.append(select)
    #print (list_mmsi_basetime)
    #print (list1)

    filetxt=open(outpath+shp_name[:-4]+'.txt','w')
    for i in list1:
        t = ''
        t = t + i
        # print t
        filetxt.write(t)
        filetxt.write('\n')

    filetxt.close()
    print (shp_name+'  '+'finishied!')

#print(list)