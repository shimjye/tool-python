#-*- coding: utf-8 -*-
import os
import sys
import time
import urllib.request

def do_request_web(url, param):
#     enc_text = urllib.parse.quote(addr)
#     url = site + param # 결과
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)
        return None

def do_request_get():
#     last = 877
    last = 77

    begin = 1
    end = 19
    timeVal = 1563260117473
    url = 'https://sootnoon.com/test?begin=%d&end=%d&ts=%d' % (begin, end, timeVal)
    print('shimjye: '+url)
    result = do_request_web(url, '')
    print(result)

    begin = 20
    end = 39

    while begin < last:
        timeVal = timeVal + 2
        url = 'https://sootnoon.com/test?begin=%d&end=%d&ts=%d' % (begin, end, timeVal)
        print('shimjye: ' + url)
        begin = begin + 20
        end = end + 20
        result = do_request_web(url, '')
        print(result)
        time.sleep(1.5)

# main
do_request_get()
