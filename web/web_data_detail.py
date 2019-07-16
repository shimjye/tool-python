#-*- coding: utf-8 -*-
import os
import sys
import time
import urllib.request
import json
import re
from bs4 import BeautifulSoup

site = 'https://sootnoon.com/test/'
test = 'key'

def do_request_web(url):
#     enc_text = urllib.parse.quote(addr)
#     url = site + param # 결과
    request = urllib.request.Request(url)
    # request.add_header("X-Naver-Client-Id",client_id)
    response = urllib.request.urlopen(request)

    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)
        return None

def to_text_val(textVal):
    textVal = re.sub('<.+?>', '', textVal, 0)
    textVal = re.sub('\n', ' ', textVal, 0)
    textVal = re.sub('[\t ]{2,}', ' ', textVal, 0)
    return textVal.strip()

def do_request_get():
    # test
    f = open("/data/python/test.html", 'r')
    result = f.read()
    print(test, result)
    do_parse(test, result)

    # list-param.txt
    # key\n
    # key\n
    # ...
    # f = open("/data/python/list-param.txt", 'r')
    # lines = f.readlines()
    # i = 0
    # for line in lines:
    #     # print(site + line)
    #     result = do_request_web(site + line)
    #     # print(result)
    #     do_parse(line, result)
    #     time.sleep(.100)
        # if i > 3:
        #     break
        # i = i + 1

    f.close()

def do_parse(line, result):
    bsObject = BeautifulSoup(result, 'html.parser')

    # category, content, business-date
    print('story', end=' || ')
    print(bsObject.find("a", class_="theme").get_text(), end=' || ')
    content = bsObject.find("ul", class_="intro_lst")
    photo1 = content.find('img')
    contentVal = str(content)
    contentVal = re.sub('<dt id="paragraphTitle">', 'shimjye-ba', contentVal, 0)
    contentVal = re.sub('</dt>', 'shimjye-bb', contentVal, 0)
    contentVal = re.sub('<br/>', 'shimjye-br', contentVal, 0)
    contentVal = re.sub('\n', ' ', contentVal, 0)
    contentVal = re.sub('<.+?>', '', contentVal, 0)
    contentVal = re.sub('shimjye-ba', '<b>', contentVal, 0)
    contentVal = re.sub('shimjye-bb', '</b><br/>', contentVal, 0)
    contentVal = re.sub('shimjye-br', '<br/>', contentVal, 0)
    print(contentVal, end=' || ')
    businessDate = bsObject.find("div", class_="use_goal").td.get_text()
    print(to_text_val(businessDate), end=' || ')
    print(line)

    # plan
    planList = bsObject.find("div", class_="use_lst").find_all('td', class_='use')
    for plan in planList :
        planTdList = plan.find_parent().find_all('td')
        if len(planTdList) > 2 :
            print('plan', end=' || ')
            print(to_text_val(plan.find_parent().find_all('td')[0].get_text()), end=' || ')
            print(to_text_val(plan.find_parent().find_all('td')[1].get_text()), end=' || ')
            print(to_text_val(plan.find_parent().find_all('td')[2].get_text()), end=' || ')
            print(line)

    # photo
    if photo1 is not None:
        print('photo', end=' || ')
        print(photo1['src'], end=' || ')
        print(line)

    photoObj = bsObject.find("div", class_="thmb_lst")
    if photoObj is not None:
        photoList = photoObj.find_all("img")
        for photo in photoList :
            print('photo', end=' || ')
            print(photo['src'], end=' || ')
            print(line)

# main
do_request_get()
