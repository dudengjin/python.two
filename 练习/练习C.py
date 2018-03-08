class Person(object):

	def __init__(self,name,weight):
		self.name = name
		self.weight = weight

	def __str__(self):
		return"我的名字叫%s,我的体重是%s"%(self.name,self.weight)

	def run(self):
		print("%s爱跑步"%str(self.name))
		self.weight -= 0.5

	def eat(self):
		print("%s爱吃东西"%str(self.name))	
		self.weight += 1


xiaoming = Person("小明",80)
xiaoming.run()
xiaoming.eat()

print(xiaoming)