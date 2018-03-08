class Aniaml(object):
	# 初始化方法
	def __init__(self):
		self.pin_zhong = "动物"

	def print_name(self):
		'''
		print(self.pin_zhong)
		'''
		print("绿叶")

class Dog(Aniaml):
	def pao(self):
		print("狗在跑")
	def cry(self):
		print("狗在哭")
	# 重写父类	
	def print_name(self):
		super().print_name()
		print("子类的")

class Cat(Aniaml):
	def miao(self):
		print("猫在喵")
	def cry(self):
		print("猫在哭")

class Zajiao(Dog,Cat):
	pass

d = Dog()
d.print_name()



a = Zajiao()
a.cry()

a = Zajiao()
a.pao()
a.miao()
a.pin_zhong = "猫狗兽"
a.print_name()

wanwan = Dog()
wanwan.pin_zhong = "狗"
wanwan.print_name()
wanwan.pao()

a = Aniaml()
a.pin_zhong = "哈巴狗"
a.print_name()


