#-*- coding: utf-8 -*-
import os
import sys
import urllib.request
import json
import time

# naver api deprecated 20190726
# shimjye key
client_id = "key"
client_secret = "key"
param = [
    '불정로 6'
]

def naver_geocode(addr):
    enc_text = urllib.parse.quote(addr)
    url = "https://openapi.naver.com/v1/map/geocode?query=" + enc_text # json 결과
    # url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)

    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)
        return None

def do_naver_geocode():
    for item in param:
        print("out name: " + item)
        result = naver_geocode(item)
        # print(result)
        json_result = json.loads(result)
        print("out lnglat: " + str(json_result["result"]["items"][0]["point"]["x"]) + ":" + str(json_result["result"]["items"][0]["point"]["y"]))
        time.sleep(.100)

# main
if __name__ == "__main__":
    do_naver_geocode()
