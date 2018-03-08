class Car(object):
	# 类属性
	count = 0
	# 类方法
	@classmethod
	def move(cls):
		print("车在移动")
	
	# 静态方法
	@staticmethod
	def benpao():
		print("车在奔跑")


	def __init__(self):
		self.color = "黄色"

Car.benpao()

a = Car()
a.benpao()


Car.move()

print(Car.count)





