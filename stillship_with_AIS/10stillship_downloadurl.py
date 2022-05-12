# import shapefile
import ee
import urllib.request
import fnmatch
import os
import sys
import csv
import time
from geopy.distance import geodesic
# from datetime import date, datetime
# from math import ceil

def cal_distance(location_info, loc_list, lon, lat):
    for k in range(len(location_info)):
        if loc_list[k]==1:
            a=location_info[k]
            lon2 = float(location_info[k].split(",")[4])
            lat2 = float(location_info[k].split(",")[3])
            dis = geodesic((lat, lon), (lat2, lon2)).m
            if dis <= 600:
                return False
    return True

ee.Initialize()
# Out_path = "F:\\GEE\\aircraft_potential_image\\"
# inputdir="F:\\GEE\\task_2_point\\"
# txt_file = open('F:\\GEE\\error.txt', 'a')
Out_path = r"F:\WHZ\Zze\SAR_vessel\stillship\image\VV\2015\tif\\"
input_txt = r'F:\WHZ\Zze\SAR_vessel\stillship\2015\\'
months = os.listdir(input_txt)[:12]


filenames = ['all.txt']
# txt_file = open('C:\\GEE\\image_download_error.txt', 'a')
for filename in filenames:

    for month in months:

        #if filename.find('AIS201707') != -1:
        f = open(os.path.join(input_txt,month,filename))
        location_info = f.readlines()
        location_len = len(location_info)
        loc_list = [0] * location_len
        #p = f.readlines()
        for i,loc in enumerate(location_info):
            p1 = loc.strip().split(',')
            lat = float(p1[3])
            lon = float(p1[4])
            SAR_name = str(p1[5])
            basetime = str(p1[2])
            id = str(p1[0])
            basetime1 = basetime.replace(':', '')
            IDD = 'COPERNICUS/S1_GRD/' + SAR_name   # COPERNICUS/S1_GRD数据集
            Out_id = SAR_name + '_' + id
            try:
                geometry = ee.Geometry.Polygon([[[lon - 0.01, lat + 0.01], [lon + 0.01, lat + 0.01],
                                                 [lon + 0.01, lat - 0.01], [lon - 0.01, lat - 0.01],
                                                 [lon - 0.01, lat + 0.01]]])
                # geometry=ee.Geometry.Point([lon,lat]).buffer(1000)
                image = ee.Image(IDD).clip(geometry)
                b4 = image.select('VV')
                # b4=image
                crs = b4.projection().crs().getInfo()
                # scale = b4.projection().nominalScale().getInfo()
                scale = 10
                istrue = cal_distance(location_info, loc_list, lon, lat)
                if istrue:
                    image_link = b4.getDownloadUrl({
                        'name': Out_id,
                        'crs': crs,
                        'scale': scale
                    })
                    print(Out_id)
                    Out_image_name = Out_path + Out_id + '.zip'
                    isExist = os.path.exists(Out_image_name)
                    if not isExist:

                        urllib.request.urlretrieve(image_link, Out_image_name)
                        loc_list[i] = 1
                    # txt_file.writelines(['\n', str(filename)])
                    # print(Out_id)
                    else:
                        loc_list[i] = 1
                        print(Out_image_name + '   done!')
                        continue
            except:
                print('Error')

                ee.Initialize()
                pass

