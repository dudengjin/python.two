
class Tool(object):
	count = 0
	def __init__(self,name):
		self.name = name
		
		Tool.count += 1

gai_zhui = Tool("改锥")
luo_si_dao = Tool("螺丝刀")

print(Tool.count)
print(gai_zhui.count)
print(luo_si_dao.count)



class Tool(object):
	count = 0
	def __init__(self,name):
		self.name = name
		
		Tool.count += 1

	@classmethod
	def tool_show_count(cls):
		print("创建了%d"%Tool.count)
		print("创建了%d"%cls.count)



gai_zhui = Tool("改锥")
luo_si_dao = Tool("螺丝刀")
Tool.tool_show_count()





