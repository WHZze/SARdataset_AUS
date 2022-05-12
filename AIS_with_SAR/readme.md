#### 1SAR_AUS_intersect.py

SAR图像与AUS领土相交

#### 2SAR_AUS_Erase.py

将存在AIS的区域以外的SAR图像擦除

#### 3read_time.py

读取SAR图像时间区间

#### 4better_txt.py

合并相同的时间，形成SAR图像时间段

#### 5invoke_add_field_element.py

对AIS数据增加DAY属性，便于下面进行分类

#### 6reshape_record.py

规范化TIMESTAMP属性

#### 7split_shp_day.py

将AIS数据从天分到日

#### 8time_filter.py

时间筛选 10s

#### 9points_area_filter.py

空间筛选

#### 10time_filter.py

第二次时间筛选

#### 11shp_txt.py

将需要下载的数据写入txt文件，(FID,CRAFT_ID,TIMESTAMPLAT,LON,Name)

#### 12ship_downloadurl1.py

联网下载数据