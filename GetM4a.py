"""
Created on 2019-4-20
@author: tsz
"""
import re
import os
# import sys
import requests
import urllib.request as req

def m4aDown(url):
    page = req.urlopen(url)
    htmlSrc = page.read()
    htmlStr = htmlSrc.decode()
    pat = re.compile(r'http://\D\D\.stream.+m4a')
    urlList = re.findall(pat, htmlStr)
    if len(urlList) < 0:
        print('m4a file Not Found!\n')
        return
    path = 'd:/m4a'
    if not os.path.exists(path):
        os.mkdir(path)
    file = requests.get(urlList[0])
    with open(path+'/music.m4a','wb') as code:
        code.write(file.content)
# print(sys.path[0])
url = input('Enter Url:\n')
m4aDown(url)

    
