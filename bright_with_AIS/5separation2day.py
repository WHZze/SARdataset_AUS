# _*_coding:utf-8_*_
# @Time : 2022/1/3 0:22
# @Author : Zze
# @File : separation2day.py
# @Software : PyCharm
import os
import fnmatch
import shutil


input = r'F:\WHZ\Zze\NEW\PLAT2\\'
years = ['2014','2015','2016','2017','2018','2019']
months = ['01','02','03','04','05','06','07','08', '09', '10', '11','12']
months3 = ['01','03','05','07','08','10','12']
months2 = ['04','06','09','11']
months1 = ['02']
days1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']
days2 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
days3 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']




for year in years:
    os.mkdir(input+year)
    print(year+' is made!')


filenames = os.listdir(input)[6:]
for filename in filenames:
    #years = ['2014', '2015', '2016', '2017', '2018', '2019']
    for year in years:
        if filename[17:21] == year:
            shutil.move(input+filename,input+year+'\\')
            print(filename + " is moved!")


#months = ['01','02','03','04','05','06','07','08', '09', '10', '11','12']
for year in years:
    if year == '2014':
        months = months[-3:]
    else:
        months =['01','02','03','04','05','06','07','08', '09', '10', '11','12']
    for month in months:
        isExist = os.path.exists(input+year+'\\'+year+month)
        if not isExist:
            os.mkdir(input+year+'\\'+year+month)
            print(year+month+' is made!')



for year in years:
    filenames = os.listdir(input+year)
    for filename in filenames:
        if filename[17:21] == '2014':
            months = months[-3:]
        else:
            months =['01','02','03','04','05','06','07','08', '09', '10', '11','12']
        for month in months:
            if filename[21:23] == month:
                shutil.move(input+year+'\\'+filename, input+year+'\\'+year+month + '\\')
                print(filename + " is moved to " + year+month )


for year in years:
    if year == '2014':
        months = months[-3:]
    else:
        months =['01','02','03','04','05','06','07','08', '09', '10', '11','12']
    for month in months:
        if month in months1:
            days = days1
            for day in days:
                isExist = os.path.exists(input + year + '\\' + year + month + '\\' + year + month + day)
                if not isExist:
                    os.mkdir(input + year + '\\' + year + month + '\\' + year + month + day)
                    print(year + month + day + ' is made!')
        elif month in months2:
            days = days2
            for day in days:
                isExist = os.path.exists(input + year + '\\' + year + month + '\\' + year + month + day)
                if not isExist:
                    os.mkdir(input + year + '\\' + year + month + '\\' + year + month + day)
                    print(year + month + day + ' is made!')
        elif month in months3:
            days = days3
            for day in days:
                isExist = os.path.exists(input + year + '\\' + year + month + '\\' + year + month + day)
                if not isExist:
                    os.mkdir(input + year + '\\' + year + month + '\\' + year + month + day)
                    print(year + month + day + ' is made!')

for year in years:
    if year == '2014':
        months = months[-3:]
    else:
        months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    for month in months:
        filenames = os.listdir(input+year+'\\'+year+month)
        if month in months1:
            days = days1
            for day in days:
                for filename in filenames:
                    if filename[23:25] == day:
                        shutil.move(input+year+'\\'+year+month+'\\'+filename, input+year+'\\'+year+month+'\\'+year+month+day)
                        print(filename + " is moved to " + year+month+day )
        elif month in months2:
            days = days2
            for day in days:
                for filename in filenames:
                    if filename[23:25] == day:
                        shutil.move(input + year + '\\' + year + month + '\\' + filename,
                                    input + year + '\\' + year + month + '\\' + year + month + day)
                        print(filename + " is moved to " + year + month + day)
        elif month in months3:
            days = days3
            for day in days:
                for filename in filenames:
                    if filename[23:25] == day:
                        shutil.move(input + year + '\\' + year + month + '\\' + filename,
                                    input + year + '\\' + year + month + '\\' + year + month + day)
                        print(filename + " is moved to " + year + month + day)








