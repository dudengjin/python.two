class SweetPotato():
	def __init__(self):
		self.cookedString = ("生的")
		self.cookedLevel = 0
		self.Condmenets = []
	
	def __str__(self):
		return "地瓜状态:%s(%d),添加的作料有:%s"%(self.cookedString,self.cookedLevel,str(self.Condmenets))

	def cook(self,cooked_time):
		self.cookedLevel = cooked_time
		if cooked_time >= 0 and cooked_time < 3:
			self.cookedString("生的")
		elif cooked_time >= 3 and cooked_time < 5:
			self.cookedString("半生不熟")
		elif cook_time >= 5 and cook_time < 8:
			self.cookedString("地瓜熟了")
		elif cooked_time > 8:
			self.cookedString("烤糊了")

	def addCondmenets(self,item):
		self.Condmenets.append(item)


# 创建了一个地瓜对象
di_gua = SweetPotato()
print(di_gua)
# 开始煮地瓜啦
di_gua.cook(1)
print(di_gua)
di_gua.addCondmenets("孜然")
di_gua.cook(1)
print(di_gua)
di_gua.addCondmenets("大蒜")
di_gua.cook(1)
print(di_gua)
di_gua.addCondmenets("食盐")
di_gua.cook(1)
print(di_gua)
di_gua.addCondmenets("辣椒")


di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
