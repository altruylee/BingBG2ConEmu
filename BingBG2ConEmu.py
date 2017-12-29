#!/usr/bin/env python
# -*- coding:utf-8 -*-
# decode('gbk').encode('utf-8')
# python抓取bing页面今日图片

import requests
import json
import os
import re

def get_background_info(url):
    re = requests.get(url)
    re_content = json.loads(re.content)
    url = re_content["images"][0]["url"]
    name = re_content["images"][0]["enddate"]
    return download(url, name)

def download(url, name):
    dest = r'd:\pictures'
    url="http://cn.bing.com/"+url
    re = requests.get(url)
    raw = re.content
    path = dest + os.path.sep + name + ".jpg"
    jpg_name = name + ".jpg"
    if os.path.exists(path) is False:
        with open(dest + os.path.sep + name + ".jpg", "wb") as f:
            f.write(raw)
    return couemu(path)

def couemu(path):
	file_object = open('F:\Program Files\ConEmu\ConEmu.xml',encoding='UTF-8')
	all_the_text = file_object.readlines()
	all_the_text[331] = '<value name="BackGround Image" type="string" data="' + path + '"/>\r'
	f = open('F:\Program Files\ConEmu\ConEmu.xml','w+',encoding='UTF-8')
	f.writelines(all_the_text)
	file_object.close( )
	f.close( )

def get_background():
	root_url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-cn"
	return get_background_info(root_url)

if __name__ == '__main__':
	get_background()