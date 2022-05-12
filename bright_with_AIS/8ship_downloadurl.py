# import shapefile
import ee
import urllib.request
import fnmatch
import os
import sys
import csv
import time

# from datetime import date, datetime
# from math import ceil

ee.Initialize()
# Out_path = "F:\\GEE\\aircraft_potential_image\\"
# inputdir="F:\\GEE\\task_2_point\\"
# txt_file = open('F:\\GEE\\error.txt', 'a')

Out_path = r'F:\WHZ\Zze\NEW\Image\VH\tif\\'

input = r'F:\WHZ\Zze\NEW\result_txt\2015\\'
#input = r'F:\WHZ\Zze\NEW\result_txt\temp\20170101\\'
folders = os.listdir(input)
for folder in folders:
    filenames = os.listdir(input+folder)
    isExist = os.path.exists(Out_path+folder)
    if not isExist:
        os.mkdir(Out_path+folder)
        os.mkdir(Out_path[:-6]+'\\'+'png'+'\\'+folder)
        print(folder + '  is made')

    #filenames = ['merge_shp.txt']
    # txt_file = open('C:\\GEE\\image_download_error.txt', 'a')
    for filename in filenames:

        f = open(input+folder + '\\' + filename)
        try:
            p1 = f.readline().strip().split(',')
            while (p1 != ['']):
                lat = float(p1[1])
                lon = float(p1[2])
                SAR_name = str(p1[3])
                #basetime = str(p1[2])
                id = str(p1[0])
                #basetime1 = basetime.replace(':', '')
                IDD = 'COPERNICUS/S1_GRD/' + SAR_name
                Out_id = SAR_name + '_' + id
                #Out_id = SAR_name + '_' + basetime1 + '_' + id


                geometry = ee.Geometry.Polygon([[[lon - 0.01, lat + 0.01], [lon + 0.01, lat + 0.01], \
                                                 [lon + 0.01, lat - 0.01], [lon - 0.01, lat - 0.01],
                                                 [lon - 0.01, lat + 0.01]]])
                # geometry=ee.Geometry.Point([lon,lat]).buffer(1000)
                image = ee.Image(IDD).clip(geometry)
                b4 = image.select('VH')
                # b4=image
                crs = b4.projection().crs().getInfo()
                # scale = b4.projection().nominalScale().getInfo()
                scale = 10
                image_link = b4.getDownloadUrl({
                    'name': Out_id,
                    'crs': crs,
                    'scale': scale
                })
                print(Out_id)
                Out_image_name = Out_path+folder+'\\' + Out_id + '.zip'
                isExist = os.path.exists(Out_image_name)
                if not isExist:

                    urllib.request.urlretrieve(image_link, Out_image_name)
                # txt_file.writelines(['\n', str(filename)])
                # print(Out_id)
                else:
                    print(Out_image_name + '   done!')

                p1 = f.readline().strip().split(',')

        except:
            print('Error')
            #time.sleep(1)
            ee.Initialize()
            pass
            continue
                # p1=f.readline().strip().split(',')
        f.close()
        '''pattern = '*.txt'
            filenames_all = fnmatch.filter(os.listdir(inputdir), pattern)
            for filename in filenames_all:
                txtfilename = inputdir+filename
                with open(txtfilename, mode='r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    for row in csv_reader:
                        coord = row
    
                X = float(coord[0])
                Y = float(coord[1])
                index = filename.rfind('_')
                IDD = 'COPERNICUS/S2/'+filename[:index]     #"COPERNICUS/S1_GRD"
                Out_id = filename[:-4]
                print(Out_id)
                try:
                    geometry = ee.Geometry.Point([X, Y]).buffer(1500)
                    image = ee.Image(IDD).clip(geometry)
                    b4 = image.select('B2','B3','B4','B8')
                    crs = b4.projection().crs().getInfo()
                    scale = b4.projection().nominalScale().getInfo()
                    image_link = b4.getDownloadUrl({
                        'name': Out_id,
                        'crs': crs,
                        'scale': scale
                    })
                    Out_image_name = Out_path+Out_id+'.zip'
                    urllib.request.urlretrieve(image_link, Out_image_name)
                    txt_file.writelines(['\n', str(filename)])
                except:
                    print('Error')
                    time.sleep(10)
                    ee.Initialize()
                else:
            os.remove(txtfilename)
            print('Ok')
    txt_file.close()'''