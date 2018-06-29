# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient

# 将网红的网址存入list
weiboZhu = ['https://weibo.com/p/1005055556869758/info?mod=pedit_more', 'https://weibo.com/p/1005051810802952/info?mod=pedit_more',
'https://weibo.com/p/1005055844573935/info?mod=pedit_more',
'https://weibo.com/p/1005051246792191/info?mod=pedit_more','https://weibo.com/p/1003061549362863/info?mod=pedit_more','https://weibo.com/p/1003061720664360/info?mod=pedit_more','https://weibo.com/p/1005051140554177/info?mod=pedit_more','https://weibo.com/p/1003061875171015/info?mod=pedit_more','https://weibo.com/p/1005051713926427/info?mod=pedit_more','https://weibo.com/p/1005052878439511/info?mod=pedit_more','https://weibo.com/p/1005053948713134/info?mod=pedit_more','https://weibo.com/p/1005052040909313/info?mod=pedit_more','https://weibo.com/p/1005052560182670/info?mod=pedit_more']

# 连接数据库
client = MongoClient("localhost", 27017)
weibo = client['weibo']
weibo_bozhu = weibo['weibo_bozhu']

# 使用webdriver调用网站
driver = webdriver.Chrome()
driver.maximize_window()
for i in weiboZhu:
    driver.get(i)
    time.sleep(15)
    # 解析网站源码
    soup = BeautifulSoup(driver.page_source, "lxml")
    # css选择器选出字段
    names = soup.select('span[class="=pt_title S_txt2"]')
    details = soup.select('span[class="pt_detail"]')
    number = 0
    # 防止溢出错误
    if len(details)<=len(names):
        while number<len(details):
            print(names[number].get_text())
            print(details[number].get_text())
            # 设置存入数据库的格式
            data = {
                'message':names[number].get_text(),
                'detail':details[number].get_text().strip().split(' ')
            }
            number=number+1
            weibo.weibo_bozhu.insert_one(data)
    else:
        while number<len(names):
            print(names[number].get_text())
            print(details[number].get_text())
            data = {
                'message':names[number].get_text(),
                'detail':details[number].get_text().strip().split(' ')
            }
            number=number+1
            # 插入数据
            weibo.weibo_bozhu.insert_one(data)
