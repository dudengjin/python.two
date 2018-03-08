class Person(object):
	def __init__(self,name):
		self.name = name 

	def eat(self):
		print("%s吃饭"%self.name)	

class Women(Person):

	def eat(self):
		print("%s在餐厅吃饭"%self.name)	

class Man(object):
	
	def __init__(self,name):
		self.name = name

	def Women_eat(self,Women):
		print("%s和%s在餐厅吃饭"%(self.name,Women.name))	


xueer = Person("雪儿")
xueer.eat()
xiaoxiao = Man("笑笑")
xiaoxiao.Women_eat(xueer)