class SweetPotato(object):
	def __init__(self):
		 # 地瓜的生熟程度 
		self.cookedLever = 0
		 # 返回给用户的字符串
		self.cookedStr = '生的'
		 # 地瓜配料列表
		self.condiments = [] 

	
	def __Str__(self):
		msg = ','
		msg = self.cookedStr
		if len(self.condiments) > 0:

			
			for test in self.condiments:
				msg = msg + test
			
		return_msg = ('当前的地瓜是%s，调料有%s'%(self.cookedStr,msg)

		return return_msg
	

	def addCondiments(self,name):
		self.condiments.append(name)


	
	# 添加烤地瓜的方法，传时间
	def cook(self,time):
		
		self.cookedLever += time
		if self.cookedLever > 8:
			self.cookedStr = '烤成炭了'
		elif self.cookedLever > 5:
			self.cookedStr = '烤好了'
		elif self.cookedLever > 3:
			self.cookedSr = '半生不熟'
		else:
			self.cookedStr = '生的'




msg_kaodigua = SweetPotato()


msg_kaodigua.cook(3) 
msg_kaodigua.addCondiments('番茄酱') 
print(msg_kaodigua)
msg_kaodigua.cook(1)
msg_kaodigua.addCondiments('沙拉酱') 
print(msg_kaodigua)


