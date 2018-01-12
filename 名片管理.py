tip = "个人名片:管理系统"
print(tip.center(20,"*"))

list = []
dic = {}

def card():
	
			
	action = int(input("请输入功能:1 增加 2 查询 3 删除 4 修改  5 退出"))
	if action == 1:
				
		name = input("请输入姓名")
		age = input("请输入年龄")
		sex = input("请输入性别")
		job = input("请输入工作")
		loction = input("请输入地址")
		dic["name"] = name
		dic["age"] = age
		dic["sex"] = sex 
		dic["job"] = job
		dic["loction"] = loction 
		list.append(dic)
		print(list)
		for i in list:
			for k,v in i.items():
				print("%s:%s"%(k,v))

def show_card():
	elif action == 2:
				
		message = input("请输入要查询的信息")
		for i in message:		
			print(message)
		
def del_card():
		
	elif action == 3:
	name = input("请输入要删除的名字")
	x = 0
	for dic in list:
		if dic["name"]== name:
			del list[x]
		else:
			x += 1
				ming = input("请输入要查询的名字")
				for dic in list:
					if ming == dic["name"]
						print("%s"%dic["name"])

def	amend_card():	
	elif action == 4:
		name = input("请输入要修改的名字")
		x = 0
		for dic in list:
			if dic["name"]== name:
				del list[x]
			else:
				x += 1
			ming = input("请输入要查询的名字")
			for dic in list:
				if ming == dic["name"]
					print("%s"%dic["name"])
	
def quit_card():		
	elif action == 5:        
		print("退出")
		return
