# -*- coding: utf-8 -*-
import urllib.request
import json
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from PIL import Image, ImageEnhance
from bs4 import BeautifulSoup

weiboZhu = ['https://weibo.com/p/1005055556869758/info?mod=pedit_more', 'https://weibo.com/p/1005051810802952/info?mod=pedit_more',
'https://weibo.com/p/1005055844573935/info?mod=pedit_more',
'https://weibo.com/p/1005051246792191/info?mod=pedit_more','https://weibo.com/p/1003061549362863/info?mod=pedit_more','https://weibo.com/p/1003061720664360/info?mod=pedit_more','https://weibo.com/p/1005051140554177/info?mod=pedit_more','https://weibo.com/p/1003061875171015/info?mod=pedit_more','https://weibo.com/p/1005051713926427/info?mod=pedit_more','https://weibo.com/p/1005052878439511/info?mod=pedit_more','https://weibo.com/p/1005053948713134/info?mod=pedit_more','https://weibo.com/p/1005052040909313/info?mod=pedit_more','https://weibo.com/p/1005052560182670/info?mod=pedit_more']

file = open(r'D:\comPython\jessiecaicai\z.txt', 'a', encoding='utf-8')
driver = webdriver.Chrome()
driver.maximize_window()
for i in weiboZhu:
    driver.get(i)
    time.sleep(15)
    soup = BeautifulSoup(driver.page_source, "lxml")

    names = soup.select('span[class="=pt_title S_txt2"]')
    details = soup.select('span[class="pt_detail"]')
    number=0
    if len(details)<=len(names):
        while number<len(details):
            print(names[number].get_text())
            file.writelines(names[number].get_text())
            file.writelines('\n')

            print(details[number].get_text())
            file.writelines(details[number].get_text().strip().split(' '))
            file.writelines('\n')
            number=number+1
    else:
        while number<len(names):
            print(names[number].get_text())
            file.writelines(names[number].get_text())
            file.writelines('\n')
            print(details[number].get_text())
            file.writelines(details[number].get_text().strip().split(' '))
            file.writelines('\n')
            number=number+1
file.close
