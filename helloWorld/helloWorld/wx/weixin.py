# -*- coding: utf-8 -*-
from django.http import HttpResponse
 

class WeiXinIF(object):
	"""docstring for WeiXinIF"""
	def __init__(self):


	def weixin(self,request):
		#判断请求类型
		if request.method == 'GET':#get请求
			signature = request.GET['signature']
			timestamp = request.GET['timestamp']
			nonce = request.GET['nonce']
			token = 'weixinlz'

		else:#post请求

