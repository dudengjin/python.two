class House_item(object):
	def __init__(self,name,area):
		self.name = name 
		self.area = area

	def __str__(self):
		return "家具名字:%s,占地面积是:%s"%(self.name,self.area)

class House:
	def __init__(self,house_type,area):
		self.house_type = house_type
		self.area = area
		self.free_area = area
		self.item_list = []

	def __str__(self):

		return ("户型是:%s,总面积是:%.2f, 剩余面积是:%.2f,家具:%s"%(self.house_type,self.area,self.free_area,self.item_list))

	def add_item(self,item):
		print("添加到:%s"%item.name)
		if float(item.area) > self.free_area:
			print("%s的面积太大,不能添加到房子中"%item.name)
			return
		self.item_list.append(item.name)
		self.free_area -= float(item.area)

bed = House_item("席梦思","4")
chest = House_item("衣柜","2")
table = House_item("餐桌","1.5")
print(bed)
print(chest)
print(table)

M_huose = House("两室一厅",80)
M_huose.add_item(bed)
M_huose.add_item(chest)
M_huose.add_item(table)

print(M_huose)



