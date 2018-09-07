#-*- coding: utf-8 -*-

param = [
'경기도 성남시 분당구 불정로 6 그린팩토리'
,'127.1052133:37.3595316'
]

query = "UPDATE table1 SET lng = {0}, lat = {1} WHERE CONCAT(address, ' ',address_detail) = '{2}';"
row_num = 0;
lng = 0.0;
lat = 0.0;
addr = '';

# main
for item in param:
    # print item
    if row_num == 0:
        addr = item
        row_num += 1
    elif row_num == 1:
        item_split = item.split(':')
        lng = item_split[0]
        lat = item_split[1]
        print(query.format(lng, lat, addr))
        row_num = 0
