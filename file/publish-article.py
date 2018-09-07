#-*- coding: utf-8 -*-
import shutil
import os

def copytree(src, dist):
    try:
        shutil.rmtree(dist)
    except OSError as ex:
        print('OS error: {0}'.format(ex))
  
    try:
        shutil.copytree(src, dist)
    except OSError as ex:
        print('OS error: {0}'.format(ex))

def makereadme(dist, basedir):
    if os.path.isdir(dist):
        if os.path.exists(dist + '/README.md'):
            os.remove(dist + '/README.md')
        f = open(dist + '/README.md', 'w')
        f.write('# ' + basedir + '\n\n')
    
        dirarr = os.listdir(dist)
        dirarr = sorted(dirarr, key=str.lower)
        for path in dirarr:
            if path == 'images' or path == 'README.md':
                continue
            name = makereadme(dist + '/' + path, basedir + '/' + path)
            f.write('- [' + name + '](' + path + ')\n')

        f.close()
    
        print('dir: ' + basedir)
        return basedir + '/'
    else:
        print('file: ' + basedir)
        return basedir


# main process

title='# 정확하지 않을 수 있는 개인적인 생각 기록.'
src='../article'
dist='../../shimjye.github.io/article'

copytree(src, dist)
makereadme(dist, 'article')
