#-*- coding: utf-8 -*-
import os
import sys
import errno
from PIL import Image

# image resize
# pip3 install image

params = [
    'H000000155396/253558.jpg'
    ,'H000000155654/121650.png'
    ,'H000000155231/202233.png'
    ,'H000000154673/923371.png'
]
source = '/data/python/images-story-first/'
target = '/data/python/images-story-first-re/'

def mkdir_p(path):
    try:
        os.makedirs(path, exist_ok=True) #python >= 3.2
    except OSError as exc: #Python > 2.5
        raise #기존 디렉토리에 접근이 불가능 한 경우

def do_main():
    f = open("/data/python/file-image.txt", 'r')
    lines = f.readlines()
    i = 0
    for item in lines:
        item = item.rstrip('\n')
        image = Image.open(source + item)
        
        width, height = image.size
        if width > 2048:
            resize_image = image.resize((2048, (int)(height * 2048 / width)), Image.ANTIALIAS)
        else:
            resize_image = image

        pathName = item[:item.find("/")]
        fileName = item[item.find("/"):item.find(".")]
        # extName = item[item.find("."):]
        print(pathName)
        print(fileName)
        # print(extName)
        
        mkdir_p(target+pathName)
        if not resize_image.mode == 'RGB':
            rgb_im = resize_image.convert('RGB')
            rgb_im.save(target+pathName+fileName+'.jpg', 'JPEG', quality=70)
        else:
            resize_image.save(target+pathName+fileName+'.jpg', 'JPEG', quality=70)
        # image.save(target+pathName+fileName+'.png', optimize=True, quality=95)

        # if i > 3: break
        print(i)
        i = i + 1
    
    f.close()

# main
do_main()
