class Tool(object):
	# 使用赋值语句，定义类属性，记录创建工具对象的总数
	count = 0
	def __init__(self,name):
		self.name = name
		# 类属性做一个计数
		Tool.count += 1

# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

print("现在创建了%d个工具"%Tool.count)
		



# 类方法用修饰器@classmethod来标识,
@classmethod
	def 类方法名(cls):
		pass




@classmethod
	def show_tool_count(cls):
	'''显示工具对象的总数'''
	print("工具对象的总数%d"%cls.count)		




# 静态方法需要用修饰器@staticmethod来标识，告诉解释器这是一个静态方法
@staticmethod
	def 静态方法名():
		pass	



class Women:
	def __init__(self,name):
		self.name = name
		self.__age = 18
	
	def __secret(self):
		print("我的年龄是%d"%self.__age)

xiaofang = Women("小芳")
# 私有属性，外部不能直接访问
print(xiaofang._Women__age)
# 私有方法，外部不能直接调用
xiaofang._Women__secret()		