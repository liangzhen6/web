# -*- coding: utf-8 -*-
import requests
import json
import random

class JiQiRen(object):
	"""docstring for JiQiRen"""
	def __init__(self):
		# super(JiQiRen, self).__init__()
		# self.arg = arg
		self.apiKey = 'afc5381cb76f488bbe8b571da3075ca6'
		self.url = 'http://www.tuling123.com/openapi/api'

	def getData(self,title,userid = None):
		if userid==None:
			userid = 7215217758991
		headers = {'content-type':'application/json'}
		payload = {'key':self.apiKey,'info':title,'userid':str(userid)}
		try:
			resp = requests.post(self.url, data = json.dumps(payload), headers = headers)
			resStr = resp.json()
			if resStr['code']!=40004 or resStr['code']!=40007:
				if resStr['code'] == 100000:# 文本类
					dic = {'type':'text','text':resStr['text']}
					return dic
				elif resStr['code'] == 200000:# 链接类
					dic = {'type':'text','text':resStr['text']+'\n'+resStr['url']}
					return dic
				elif resStr['code'] == 302000:# 新闻类
					if len(resStr['list']):
						one = self.getnewshaveimage(resStr['list'])
						dic = {'type':'news','article':one['article'],'source':one['source'],'icon':one['icon'],'detailurl':one['detailurl']}
						return dic
					else:
						return '被你玩坏了!1'
				elif resStr['code'] == 308000:# 菜谱类
					# if len(resStr['list']):
					# 	one = resStr['list'][0]
					# 	dic = {'type':'news','article':one['name'],'source':one['info'],'icon':one['icon'],'detailurl':one['detailurl']}
					# 	return dic
					return '此功能还在开发中!'
				else:
					return '被你玩坏了!2'
			else:
				return '被你玩坏了!3'
		except:
			return '被你玩坏了!4'

	def getnewshaveimage(self,newsList):
		mynews = []
		for x in newsList:
			if len(x['icon']):
				mynews.append(x)
		return random.choice(mynews)


jqr = JiQiRen()

