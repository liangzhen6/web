# -*- coding=utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import time
import random

def getxh():
	headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
	num = random.randint(1,1001)
	all_url = 'http://xiaohua.zol.com.cn/new/%s.html'%(str(num))  ##开始的URL地址
	print(all_url)
	start_html = requests.get(all_url,  headers=headers)
	Soup = BeautifulSoup(start_html.text,'lxml')

	div_all = Soup.find('div',class_ = 'main')
	li_all = div_all.find('ul',class_ = 'article-list').find_all('li')

	num2 = random.randint(1,21)
	li = li_all[num2]
	title = li.find('span',class_ = 'article-title').get_text()
	des = li.find('div',class_ = 'summary-text').get_text()

	xh = title + '\n' + des
	return xh



