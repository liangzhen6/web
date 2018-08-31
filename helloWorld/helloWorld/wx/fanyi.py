# -*- coding: utf-8 -*-  
import requests
from bs4 import BeautifulSoup
import time
import random
# from getwxtoken import wxtoken
import sys,os


class FanYi(object):
	"""docstring for Fanyi"""
	def __init__(self):
		self.dowurl = 'https://api.weixin.qq.com/cgi-bin/media/get'
		self.upurl = 'http://api.weixin.qq.com/cgi-bin/media/voice/translatecontent'
		# self.access_token = wxtoken.getToken()
		self.access_token = '7_3u6W_d_wlFEPXIdN8eJlEQudN39jM_yiDzXXIHZBS0uQ3tv5DyOX8bgAkveQO9o8_EPnaUA77hFWvrKd-NlCYdYFJstBb0pLUbKcq1IFtqSJorLChXOLcwddFRUQPKeADAUTO'
		if self.access_token is None:
			hostname = socket.gethostname()
			ip = socket.gethostbyname(hostname)
			return self.render.reply_text(fromUser,toUser,int(time.time()),ip)


	def getfyResukt(self,mediaId,formats):
		if mediaId is not None and formats is not None:
			file = self.downloadFile(mediaId,formats)
			print(len(file))
			self.updateData(file)
			return len(file)


	def downloadFile(self,mediaId,formats):
		headers = {'content-type':'application/json'}
		payload = {'access_token':self.access_token,'media_id':mediaId}
		resp = requests.get(self.dowurl, headers = headers, params = payload)
		return resp.content
		# print(resp.content)
		# currentPath = os.path.abspath('.')
		# mypath = os.path.join(currentPath,'download')
		# dpath = os.path.join(mypath,"yuyin.%s" % (formats))
		# f = open(dpath,'wb+')
		# f.write(resp.content)
		# f.close
		# return '存取完毕'
		# 
	def updateData(self,contentData):
		headers = {'content-type':'application/json'}
		payload = {'access_token':self.access_token,'lfrom':'zh_CN','lto':'en_US'}
		# currentPath = os.path.abspath('.')
		# mypath = os.path.join(currentPath,'download')
		files = {'field1':contentData}
		resp = requests.post(self.upurl, data = payload, files = files)
		print(resp.content)

fanyi = FanYi()
fanyi.getfyResukt('tTXE3RNJ0WZ2Ym4DVI00i5VlmSoK7_x7d7J_S2HCDQeStNdDw_lyuujymR06NYR0','amr')
# fanyi.updateData('hello')
# print('你好')




