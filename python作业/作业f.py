class Restaurant(object):
	def __init__(self):

	# 餐馆的名字
		self.restaurant_name = '忆往昔小屋'
	# 菜品
		self.cuisine = '绿豆糕'

	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine)

	def open_restaurant(self):
		print('%s正在营业'%self.restaurant_name）

r1 = Restaurant()
# 调用属性
a = r1.restaurant_name
b = r1.cuisine
# 调用方法
r1.describe_restaurant
r1.open_restaurant









