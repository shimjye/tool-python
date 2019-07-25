#-*- coding: utf-8 -*-
import os
import sys
import urllib.request
import json
import time

# kakao local https://developers.kakao.com/docs/restapi/local
# HTTP/1.1 200 OK
# Content-Type: application/json;charset=UTF-8
# {
#   "meta": {
#     "total_count": 4,
#     "pageable_count": 4,
#     "is_end": true
#   },
#   "documents": [
#     {
#       "address_name": "전북 익산시 부송동 100",
#       "y": "35.97664845766847",
#       "x": "126.99597295767953",
#       "address_type": "REGION_ADDR",
#       "address": {
#         "address_name": "전북 익산시 부송동 100",
#         "region_1depth_name": "전북",
#         "region_2depth_name": "익산시",
#         "region_3depth_name": "부송동",
#         "region_3depth_h_name": "삼성동",
#         "h_code": "4514069000",
#         "b_code": "4514013400",
#         "mountain_yn": "N",
#         "main_address_no": "100",
#         "sub_address_no": "",
#         "zip_code": "570972",
#         "x": "126.99597295767953",
#         "y": "35.97664845766847"
#       },
#       "road_address": {
#         "address_name": "전북 익산시 망산길 11-17",
#         "region_1depth_name": "전북",
#         "region_2depth_name": "익산시",
#         "region_3depth_name": "부송동",
#         "road_name": "망산길",
#         "underground_yn": "N",
#         "main_building_no": "11",
#         "sub_building_no": "17",
#         "building_name": "",
#         "zone_no": "54547",
#         "y": "35.976749396987046",
#         "x": "126.99599512792346"
#       }
#     },
#     ...
#   ]
# }

client_id = 'key' # key
param = [
    '전북 삼성동 100'
]

def kakao_local_search_address(addr):
    enc_text = urllib.parse.quote(addr)
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + enc_text # json 결과
    request = urllib.request.Request(url)
    request.add_header('Authorization','KakaoAK ' + client_id)
    response = urllib.request.urlopen(request)

    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        return response_body.decode('utf-8')
    else:
        print('Error Code:' + rescode)
        return None

def do_out(result):
    json_result = json.loads(result)
    print('out-lnglat|' + str(json_result['documents'][0]['x']) + '|' + str(json_result['documents'][0]['y']) \
        + '|' + str(json_result['documents'][0]['address']['address_name']) \
        + '|' + str(json_result['documents'][0]['road_address']['address_name']))

def do_main():
    f = open("/data/python/sweb/kakao-list.txt", 'r')
    lines = f.readlines()
    i = 0
    for item in lines:
        print('out-name|' + item)
        result = kakao_local_search_address(item)
        print(result)

        do_out(result)

        # if i > 3: break
        i = i + 1
        time.sleep(.100)

def do_test():
    print('test')
    # f = open("/data/python/sweb/kakao-test.txt", 'r')
    # result = f.read()
    result = '{"documents":[{"address":{"address_name":"전북 익산시 부송동 100","b_code":"4514013400","h_code":"4514069000","main_adderss_no":"100","main_address_no":"100","mountain_yn":"N","region_1depth_name":"전북","region_2depth_name":"익산시","region_3depth_h_name":"삼성동","region_3depth_name":"부송동","sub_adderss_no":"","sub_address_no":"","x":"126.99597295767953","y":"35.97664845766847","zip_code":"570972"},"address_name":"전북 익산시 부송동 100","address_type":"REGION_ADDR","road_address":{"address_name":"전북 익산시 망산길 11-17","building_name":"","main_building_no":"11","region_1depth_name":"전북","region_2depth_name":"익산시","region_3depth_name":"부송동","road_name":"망산길","sub_building_no":"17","undergroun_yn":"N","underground_yn":"N","x":"126.99599512792346","y":"35.976749396987046","zone_no":"54547"},"x":"126.99597295767953","y":"35.97664845766847"},{"address":{"address_name":"전북 익산시 임상동 100","b_code":"4514013200","h_code":"4514069000","main_adderss_no":"100","main_address_no":"100","mountain_yn":"N","region_1depth_name":"전북","region_2depth_name":"익산시","region_3depth_h_name":"삼성동","region_3depth_name":"임상동","sub_adderss_no":"","sub_address_no":"","x":"126.98026713191277","y":"35.98166138482209","zip_code":"570380"},"address_name":"전북 익산시 임상동 100","address_type":"REGION_ADDR","road_address":null,"x":"126.98026713191277","y":"35.98166138482209"},{"address":{"address_name":"전북 익산시 정족동 100","b_code":"4514013100","h_code":"4514069000","main_adderss_no":"100","main_address_no":"100","mountain_yn":"N","region_1depth_name":"전북","region_2depth_name":"익산시","region_3depth_h_name":"삼성동","region_3depth_name":"정족동","sub_adderss_no":"","sub_address_no":"","x":"127.00208907550905","y":"35.98265074446077","zip_code":"570370"},"address_name":"전북 익산시 정족동 100","address_type":"REGION_ADDR","road_address":null,"x":"127.00208907550905","y":"35.98265074446077"}],"meta":{"is_end":true,"pageable_count":3,"total_count":3}}'
    do_out(result)
    # f.close()

if __name__ == '__main__':
    do_main()
#     do_test()
