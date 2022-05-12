# -*- coding: UTF-8 -*-
import arcpy
import os
import fnmatch
import time
import datetime


#读取澳大利亚sar中成像时间


#找到shp文件
def File_name(file_dir):
    file_list=[]
    files=os.listdir(file_dir)  # 用于返回指定的文件夹包含的文件或文件夹的名字的列表
    for file in files:
        if file[-3:]=='shp':
            file_list.append(file)
    return file_list


#file=r'F:\lab\boat_task\SAR_USA_Intersect\20170101.shp'

#读取shp文件的TIME属性并且返回时间列表
def read_Time(fc,in_dir):
    Time_list=[]
    Time_list1=[]
    rows=arcpy.SearchCursor(in_dir+ '\\' + fc)
    delta=datetime.timedelta(seconds=10)  # 前后间隔10s
    for row in rows:
        Time_s=str(row.TIME)
        Time_e=str(row.TIME1)
        Time_s=Time_s[0:2]+':'+Time_s[2:4]+':'+Time_s[4:6]
        Time_e = Time_e[0:2] + ':' + Time_e[2:4] + ':' + Time_e[4:6]
        #print Time
        Time_s=datetime.datetime.strptime(Time_s,'%H:%M:%S')
        Time_e = datetime.datetime.strptime(Time_e, '%H:%M:%S')
        #print Time
        Time1=Time_s-delta
        Time2=Time_e+delta
        #Time=str(Time)
        Time1 = str(Time1)
        Time2 = str(Time2)
        Time_list.append(Time1[-8:]+','+Time2[-8:])     #按照原始属性表取值
        Time_list1=list(set(Time_list))
        Time_list1.sort()     #排序

    return Time_list1


#针对每一个shp文件创建txt
def creat_txt(file):

    full_path=outpath+foldername+"\\"+file[0:8]+'.txt'
    filetxt=open(full_path,'w')       #创建并且写入txt文件
    Time_list=read_Time(file,inpath+foldername)

    for i in Time_list:             #将列表转为字符串再写入txt
        t=''
        t=t+i
        #print t
        filetxt.write(t)
        filetxt.write('\n')

    filetxt.close()
    print file+'  finished!'

if __name__=='__main__':
    start=time.time()
    inpath = r'F:\WHZ\Zze\SAR_vessel\SAR_AUS\\'
    outpath = r'F:\WHZ\Zze\SAR_vessel\SAR_Time_txt\\'
    foldernames = os.listdir(inpath)[:12]
    for foldername in foldernames:
        os.mkdir(outpath + foldername)
        print(foldername + '  is made')
        filenames=File_name(inpath+foldername)
        for file in filenames:
            #if file.find('20170101')==-1:
            creat_txt(file)


end=time.time()
print ('time is %d second'%(end-start))
