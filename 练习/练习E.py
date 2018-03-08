# 私有方法
class Women:
	def __init__(self,name):
		self.name = name
		self.__name = 18

	def __secret(self):
		print("我的年龄是%d"%self.__age)

xiaofang = Women("小芳")
# print(xiaofang.__age)  # 私有属性，外部不能直接访问
# xiaofang.__secret()  # 私有方法，外部不能直接调用

print(xiaofang._Women__age)
xiaofang._Women__secret()
