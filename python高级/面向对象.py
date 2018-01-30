# 汽车类
class Car:
	def __init__(self,mewname):
		self.name = mewname
		self.price = '30000'
	
	def move(self):
		print(self.name,'移动')
	def toot(self):
		print('鸣叫')

# 创建对象
red_car = Car('玛莎拉蒂')
red_car.move()
red_car.color = 'red'

print(id(red_car),red_car.color)


blue_car = Car('凯迪拉克')
blue_car.toot()
blue_car.color = 'blue'

print(id(blue_car),blue_car.color)


yellow_car = Car('林肯')
yellow_car.move()
yellow_car.toot()

yellow_car.color = 'yellow'

print(id(yellow_car),yellow_car.color)
