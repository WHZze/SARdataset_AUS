# _*_coding:utf-8_*_
# @Time : 2021/12/23 10:30
# @Author : Zze
# @File : stationary_ship5.py
# @Software : PyCharm
import os
from osgeo import osr
import shapefile  # 使用pyshp库
import datetime
import fnmatch

def Create_shp(fields1,IDList,IDShape,outshpname):
    w = shapefile.Writer(outshpname)
    w.autoBalance = 1  # 自动平衡，防止写入记录格式不正确
    a=1
    for field1 in fields1:
        w.field(field1[0],field1[1],field1[2],field1[3])  # 给文件写入格式
    for line1,line2 in zip(IDList,IDShape):             # zip() 将对象中的元素打包成元组，然后返回一个列表
        part = list(line2.points[0:2][0])                 # list 将元组转换为列表
        LON = part[0]                                     # iterShapeRecords（）方法遍历所以文件
        LAT = part[1]
        linelist = list(line1)
        w.record(*linelist)                               # *号的作用在于收集参数或者分配参数
        w.point(LON, LAT)
    w.close()
    # 定义投影
    proj = osr.SpatialReference()
    proj.ImportFromEPSG(4326)  # 4326-GCS_WGS_1984; 4490- GCS_China_Geodetic_Coordinate_System_2000
    wkt = proj.ExportToWkt()
    # 写入投影
    f = open(outshpname.replace(".shp", ".prj"), 'w')
    f.write(wkt)  # 写入投影信息
    f.close()  # 关闭操作流

inpath = r"F:\WHZ\Zze\SAR_vessel\stillship\2018\\"
months = os.listdir(inpath)[8:9]
for month in months:
    filenames = fnmatch.filter(os.listdir(inpath+month),'AIS*.shp')
    #filenames = ['AIS20170101.shp']


    for filename in filenames:
        #if filename[:3] != 'AIS':
        shpFile = inpath+month+'\\'+filename
        isExist = os.path.exists(inpath + month+'\\'+filename[:-4])
        if not isExist:
            os.mkdir(inpath +month+'\\'+ filename[:-4])
            print(filename[:-4] + '  is made')
        ouputpath = inpath + month+'\\'+filename[:-4] + '\\'

        sf = shapefile.Reader(shpFile)
        fields = sf.fields
        fields1 = []
        for k,field in enumerate(fields):           # enumerate将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
            if k!=0:
                fields1.append(field)
        del fields
        length=sf.numRecords
        IDList=[]
        IDShape=[]
        #pattern="%Y%m%d"

        shapeRecords = sorted(sf.shapeRecords(), key = lambda shapeRecords: shapeRecords.record['CRAFT_ID'])
        print("ALL records: "+str(length))

        recordnums=0

        starttime = datetime.datetime.now()
        # for records in records:

        for i,shaoeRecord in enumerate(shapeRecords):


            if i==sf.numRecords-1: #每个月最后一个日期的写入
                IDList.append(shaoeRecord.record)
                IDShape.append(shaoeRecord.shape)

                recordnums = recordnums + len(IDList)
                # 创建新的shapefile文件
                Create_shp(fields1, IDList, IDShape, ouputpath+str(shaoeRecord.record[1])[:-2] + '.shp')
                IDList = []
                IDShape = []
                print(str(shaoeRecord.record[1])[:-2] + '.shp' + " " +  " !")
            else:
                Time1 = str(shaoeRecord.record[1])
                Time2 = str(shapeRecords[i+1].record[1])


                if Time1==Time2:
                    IDList.append(shaoeRecord.record)
                    IDShape.append(shaoeRecord.shape)
                else:
                    #创建新的shapefile文件
                    IDList.append(shaoeRecord.record)
                    IDShape.append(shaoeRecord.shape)

                    recordnums=recordnums+len(IDList)
                    Create_shp(fields1, IDList, IDShape,ouputpath+str(shaoeRecord.record[1])[:-2]+'.shp')
                    IDList=[]
                    IDShape=[]
                    print(str(shaoeRecord.record[1])[:-2]+'.shp' + " " + " !")


            endtime = datetime.datetime.now()
            print("Time: "+str((endtime - starttime).seconds))
            print(recordnums)