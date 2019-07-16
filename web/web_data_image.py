#-*- coding: utf-8 -*-
import os
import sys
import errno
import time
import random
import urllib.request

def mkdir_p(path):
    try:
        os.makedirs(path, exist_ok=True) #python >= 3.2
    except OSError as exc: #Python > 2.5
        raise #기존 디렉토리에 접근이 불가능 한 경우

# thexigner happybean 작업 - image
def do_request_get():
    # photo || https://sootnoon.com/image-file-path || key
    f = open("/data/python/photo-list.txt", 'r')
    lines = f.readlines()
    i = 0
    for line in lines:
        lineSplit = line.split('||')

        ext = lineSplit[1].lower().rfind('jpg')
        if ext == -1:
            ext = lineSplit[1].lower().rfind('jpeg')
            if ext == -1:
                ext = 'png'
            else:
                ext = 'jpg'
        else:
            ext = 'jpg'
        # print(ext)

        # print()
        # print(lineSplit[1].strip())
        enc_text = urllib.parse.quote(lineSplit[1].strip()[8:-10])
        # enc_text = lineSplit[1].strip()[8:]
        url = str('https://'+enc_text+'?type=w720')
        name = 'images/'+lineSplit[2].strip()+'/'+str(random.randrange(1,999999))+'.'+ext
        # url = str('https://'+lineSplit[1].strip()[8:]+'/'+str(random.randrange(1,9999))+'.'+ext).encode('utf-8')
        print(url)
        print(name)
        mkdir_p('images/'+lineSplit[2].strip())
        urllib.request.urlretrieve(url, name)

        # if i > 1:
        #     break
        i = i + 1
        print ('count' + str(i))

    f.close()

# main
do_request_get()
