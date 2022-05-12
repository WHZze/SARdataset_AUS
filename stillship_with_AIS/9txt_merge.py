# _*_coding:utf-8_*_
# @Time : 2021/12/13 22:23
# @Author : Zze
# @File : txt_merge.py
# @Software : PyCharm
import os
import fnmatch

txtpath = r'F:\WHZ\Zze\SAR_vessel\stillship\2015\\'
months = os.listdir(txtpath)

for month in months:
    #获取当前文件夹中的文件名称列表
    filenames=fnmatch.filter(os.listdir(txtpath+month),'merge*.txt')
    #打开当前目录下的result.txt文件，如果没有则创建
    f=open(txtpath+month+'\\'+'all.txt','w')
    #先遍历文件名
    for filename in filenames:
        #遍历单个文件，读取行数
        for line in open(txtpath+month+'\\'+filename):
            f.writelines(line)
            #f.write('\n')
        print filename + '  is finished!'
    #关闭文件
    f.close()

