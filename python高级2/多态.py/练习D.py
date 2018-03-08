class Person(object):
	def __init__(self,name):
		self.name = name

	def eat(self):
		print(self.name + "正在吃冰激凌")

class Doudou(Person):	

	def eat(self):
		print(self.name + "在店里吃冰激凌")

class Mum(object):
	def __init__(self,name):
		self.name = name

	def eat(self,Person):
		print("%s和%s在店里吃冰激凌"%(self.name,Person.name))

xiaoxiao = Person("小小")
xiaoxiao.eat()


yuekexia = Doudou("豆豆") 

qiqi = Person("琪琪")
xiaoli = Mum("小李")
xiaoli.eat(qiqi)

xiaoli.eat(yuekexia)
