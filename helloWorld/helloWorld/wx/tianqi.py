# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import json
import random
import re


class TianQi(object):

	def get(self,url):
		header = [
			"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
 			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
 			"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
 			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
 			"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
 			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
 			"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
 			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
 			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
 			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
 			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
 			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
 			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
 			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
 			"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
		]
		headers = {'User-Agent':random.choice(header)}
				
		try:
			return requests.get(url,headers = headers)
		except :
			return None
		

	def getTianQiUrl(self,title):
		url = 'http://tianqi.2345.com/t/searchCity.php'+'?q=%s&pType=local'%(title)
		res = self.get(url)
		if res:
			li = res.json()['res']
			if len(li):
				dic = li[0]
				return dic
			else:
				return None
		else:
			return None

	def getTianQi(self,title):
		res_url = self.getTianQiUrl(title)
		if res_url == None:
			return u'查无此地,退出天气查询回复：t'
		dr = re.compile(r'<[^>]+>',re.S)
		res_title = res_url['text']
		res_title = dr.sub('',res_title)
		url = res_url['href']
		if url:
			city_url = 'http://tianqi.2345.com'+url
			print(city_url)
			res = self.get(city_url)
			try:
				Soup = BeautifulSoup(res.text,'lxml')
				div = Soup.find('div',class_ = 'week week_day7')
				ul = div.find('ul',class_ = 'clearfix has_aqi')
				li = ul.find_all('li')[0]
				today = li.find('strong').get_text()
				weather = li.find('b').get_text()
				wendu = li.find('i').get_text()
				TQ = res_title.lstrip() + '\n' + today.lstrip() + weather.lstrip() + '\n' + wendu.lstrip() 
				print(TQ)
				return TQ
			except:
				return u'查无此地,退出天气查询回复：t'
		else:
			print('查无此地')
			return u'查无此地,退出天气查询回复：t'


tqyb = TianQi()

				


