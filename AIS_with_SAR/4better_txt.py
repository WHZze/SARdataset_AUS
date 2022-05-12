# -*- coding: UTF-8 -*-

import os
import shutil
import fnmatch
import numpy as np
import datetime

in_path=r'F:\WHZ\Zze\SAR_vessel\SAR_Time_txt\\'
out_path=r'F:\WHZ\Zze\SAR_vessel\SAR_Time_better_txt\\'
starttime = datetime.datetime.now()
foldernames = os.listdir(in_path)[:12]
for foldername in foldernames:
    os.mkdir(out_path + foldername)
    print(foldername + '  is made')
    filenames=os.listdir(in_path+foldername)


    # 时间合并
    for filename in filenames:
        #if filename.find('20170103') != -1:
        flag=1
        result = []
        f = open(in_path+foldername + '\\' + filename)
        p = f.readlines()
        f.seek(0)
        if len(p) == 0:
            print (filename + ' is null!')
        elif len(p) == 1:
            shutil.copy(in_path+foldername + '\\' + filename,out_path+foldername + '\\')
            print (filename +"  only have one line")
        # result = []
        # iter_f=iter(f)      #用迭代器循环访问文件中的每一行
        # print len(iter_f)
        # head=f.readline().strip()
        else:
            p1=p2=[]
            p1 = f.readline().strip().split(',')  # 通过指定分隔符对字符串进行切片
            head=p1
            p2 = f.readline().strip().split(',')
            # print head
            # print p1[0]
            # print p1[1]
            # print p2[0]

            time1_s = datetime.datetime.strptime(p1[0], '%H:%M:%S')  # 时间转换接口 1900-01-01 00:17:40

            # print time1_s #1900-01-01 00:22:08
            time1_e = datetime.datetime.strptime(p1[1], '%H:%M:%S')
            time2_s = datetime.datetime.strptime(p2[0], '%H:%M:%S')
            time2_e = datetime.datetime.strptime(p2[1], '%H:%M:%S')
            # print time1_e
            # print time2_s
            # print time2_e

            while p2!=['']:
                delta = (time2_s - time1_e)
                while(delta <= datetime.timedelta(seconds=0)):
                    p1=p2
                    p2=f.readline().strip().split(',')
                    #print(p2)
                    if p2==[''] :
                        #print('gkggkgkgk')
                        flag = 0
                        break
                    time1_s = datetime.datetime.strptime(p1[0], '%H:%M:%S')
                    time1_e = datetime.datetime.strptime(p1[1], '%H:%M:%S')
                    time2_s = datetime.datetime.strptime(p2[0], '%H:%M:%S')
                    time2_e = datetime.datetime.strptime(p2[1], '%H:%M:%S')
                    delta = (time2_s - time1_e)

                if flag:
                    result.append(head[0]+','+p1[1])
                    #print(head[0]+','+p1[1])
                    head=p1=p2
                    p2=f.readline().strip().split(',')
                    #print(p2)
                    time1_s = datetime.datetime.strptime(p1[0], '%H:%M:%S')
                    time1_e = datetime.datetime.strptime(p1[1], '%H:%M:%S')
                    if p2!=['']:
                        time2_s = datetime.datetime.strptime(p2[0], '%H:%M:%S')
                        time2_e = datetime.datetime.strptime(p2[1], '%H:%M:%S')
                #print '12'

            result.append(head[0]+','+p1[1])
            #print(head[0]+','+p1[1])

            #print(result)

            new_file=open(out_path+foldername + '\\'+filename[0:8]+'.txt','w')

            for row in result:
                t=''
                t=t+row
                new_file.write(t)
                new_file.write('\n')
            #new_file.writelines(result)
            new_file.close()
            f.close()
            print(out_path+foldername + '\\'+filename[0:8]+'.txt    finished!')

endtime = datetime.datetime.now()
print("Time: "+str((endtime - starttime).seconds))

# 排序
'''f=open(r'F:\lab\boat_task\SAR_Time_txt\20170101.txt')
result= []
iter_f=iter(f)      #用迭代器循环访问文件中的每一行
for line in iter_f:
    result.append(line)
f.close()
result.sort()
f=open(r'F:\lab\boat_task\SAR_Time_txt\20170101.txt','w')
f.writelines(result)
f.close()


in_path = r'F:\lab\boat_task\SAR_Time_txt\\'
out_path = r'F:\lab\boat_task\SAR_Time_txt_better\\'
filenames = os.listdir(in_path)


#去除重复行
for filename in filenames:
    f=open(in_path+filename,'r')
    outfile=open(out_path+filename,'w')
    lines_seen=set()
    for line in f:
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
    f.close()
    outfile.close()'''








