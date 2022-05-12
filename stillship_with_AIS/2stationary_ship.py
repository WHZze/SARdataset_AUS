# _*_coding:utf-8_*_
# @Time : 2021/12/18 16:48
# @Author : Zze
# @File : stationary_ship1.py
# @Software : PyCharm
import shapefile
import pandas as pd
import fnmatch
import os
import time


shppath = r'F:\WHZ\Zze\SAR_vessel\stillship\2018\\'
months = os.listdir(shppath)
begin = time.time()
for month in months:

    filenames = fnmatch.filter(os.listdir(shppath+month),'*.shp')

    for filename in filenames:
        if filename[:3] != 'AIS':
            sf=shapefile.Reader(shppath+month+'\\'+filename)
            records=sf.records()
            df=pd.DataFrame(records)

            countdf = df.groupby(0).count()
            results = df.loc[df[0].isin(countdf[countdf[4] > 4].index)]
            #print(list(set(list(results[0]))))
            mylist = list(set(list(results[0])))
            mylist1 = []
            for i in mylist:
                mylist1.append(str(i))
            #print (len(mylist1))

            with open(shppath+month+'\\'+filename[-6:-4]+'.txt', 'w') as f:
                for i in mylist1:
                    t = ''
                    t = t + i
                    # print t
                    f.write(t)
                    f.write('\n')
            print (month+'\\'+filename[-6:-4]+'   is finished!')

end = time.time()
print('time is %d seconds ' % (end - begin))