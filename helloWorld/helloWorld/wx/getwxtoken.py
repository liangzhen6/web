# -*- coding: utf-8 -*-
import requests
import json
# import md5
import pylibmc
import time

class WeiXinToken(object):
	def __init__(self):
		self.url = 'https://api.weixin.qq.com/cgi-bin/token'
		self.appID = 'wx1e0fee1bb95ab7ab'
		self.secret = 'c0f9a07bbbfb2cf45e9dce419d898fa7'
		self.mc = pylibmc.Client() #初始化一个memcache实例用来保存token信息
		# grant_type   client_credential
	def getToken(self):
		if self.mc.get('myToken'):
			lastTime = int(self.mc.get('myToken')['time'])
			nowTime = int(time.time())
			if nowTime-lastTime<7000:#没有过期
				return self.mc.get('myToken')['token']
			else:#已经过期
				return self.reqToken()
		else:
			return self.reqToken()

	def reqToken(self):
		headers = {'content-type':'application/json'}
		params = {'grant_type':'client_credential','appid':self.appID,'secret':self.secret}
		try:
			resp = requests.get(self.url,params = params,headers = headers)
			jsresp = resp.json()
			if jsresp['access_token']:#成功
				nowtime = int(time.time())
				data = {'time':nowtime,'token':jsresp['access_token']}
				self.mc.set('myToken',data)
				return jsresp['access_token']
			else:
				return jsresp['errcode']
		except:
			return None
			# return '出错了'

wxtoken = WeiXinToken()

# print(wxtoken.reqToken())