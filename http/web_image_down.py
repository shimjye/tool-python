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

# image down
def do_main():
    # photo || https://sootnoon.com/image-file-path || key(dir)
    f = open("/data/python/imagedown/photo-list.txt", 'r')
    lines = f.readlines()
    i = 0
    for line in lines:
        lineSplit = line.split('||')
        extName = lineSplit[1][lineSplit[1].rfind("."):].strip()

        # param
        # enc_text = urllib.parse.quote(lineSplit[1].strip()[8:-10])
        # url = str('https://'+enc_text+'?type=w720')

        enc_text = urllib.parse.quote(lineSplit[1].strip()[8:])
        url = str('https://'+enc_text)

        name = 'images/'+lineSplit[2].strip()+'/'+str(random.randrange(1,999999))+extName
        print ('py-count|' + str(i))
        print('py-url|'+url)
        print('py-name|'+name)

        # exec
        mkdir_p('images/'+lineSplit[2].strip())
        urllib.request.urlretrieve(url, name)

        # if i > 1: break
        i = i + 1

    f.close()

# main
if __name__ == "__main__":
    do_main()
