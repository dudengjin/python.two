# 可以访问属性，或者让对象调用方法
class Cat:
	def __init__(self,new_name):
		self.name = new_name
		print("%s来了"%self.name)

	def __del__(self):
		print("%s去了"%self.name)	

	def __str__(self):
		return "我是小猫:%s"%self.name


# tom = Cat("Tom")		
# print(tom.name)
 
tom = Cat("Tom") 
print(tom)