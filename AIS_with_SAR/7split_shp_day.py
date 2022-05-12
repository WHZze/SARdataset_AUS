# _*_coding:utf-8_*_
import os
from osgeo import osr
import shapefile  # 使用pyshp库
import datetime
import fnmatch

def Create_shp(fields1,DAYList,DAYShape,outshpname):
    w = shapefile.Writer(outshpname)
    w.autoBalance = 1  # 自动平衡，防止写入记录格式不正确
    a=1
    for field1 in fields1:
        w.field(field1[0],field1[1],field1[2],field1[3])  # 给文件写入格式
    for line1,line2 in zip(DAYList,DAYShape):             # zip() 将对象中的元素打包成元组，然后返回一个列表
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

inpath = r"F:\WHZ\Zze\SAR_vessel\AUS_2016\\"
#inpath = r'F:\WHZ\Zze\SAR_vessel\test\\'
foldernames = os.listdir(inpath)[:4]
for foldername in foldernames:
    Files = fnmatch.filter(os.listdir(inpath+foldername),'*.shp')
    for File in Files:
        shpFile = inpath+foldername + '\\' + File
        ouputpath = inpath + foldername + '\\'

        sf = shapefile.Reader(shpFile)
        fields = sf.fields
        fields1 = []
        for k,field in enumerate(fields):           # enumerate将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
            if k!=0:
                fields1.append(field)
        del fields
        length=sf.numRecords
        DAYList=[]
        DAYShape=[]
        pattern="%Y%m%d"

        shapeRecords = sorted(sf.shapeRecords(), key = lambda shapeRecords: shapeRecords.record['DAY'])
        print("ALL records: "+str(length))

        recordnums=0

        starttime = datetime.datetime.now()
        # for records in records:

        for i,shaoeRecord in enumerate(shapeRecords):


            if i==sf.numRecords-1: #每个月最后一个日期的写入
                DAYList.append(shaoeRecord.record)
                DAYShape.append(shaoeRecord.shape)

                recordnums = recordnums + len(DAYList)
                # 创建新的shapefile文件
                Create_shp(fields1, DAYList, DAYShape, ouputpath+shaoeRecord.record[-1] + '.shp')
                DAYList = []
                DAYShape = []
                print(shaoeRecord.record[-1] + '.shp' + " " +  " !")
            else:
                DayTime1 = shaoeRecord.record[-1]
                DayTime2= shapeRecords[i+1].record[-1]
                Time1 = datetime.datetime.strptime(DayTime1, pattern)
                Time2 = datetime.datetime.strptime(DayTime2, pattern)

                if Time1==Time2:
                    DAYList.append(shaoeRecord.record)
                    DAYShape.append(shaoeRecord.shape)
                else:
                    #创建新的shapefile文件
                    DAYList.append(shaoeRecord.record)
                    DAYShape.append(shaoeRecord.shape)

                    recordnums=recordnums+len(DAYList)
                    Create_shp(fields1, DAYList, DAYShape,ouputpath+shaoeRecord.record[-1]+'.shp')
                    DAYList=[]
                    DAYShape=[]
                    print(shaoeRecord.record[-1]+'.shp' + " " + " !")


endtime = datetime.datetime.now()
print("Time: "+str((endtime - starttime).seconds))
print(recordnums)