adminAccount = "123456"
adminPwd = "123456"
list = []

#新增
def add():	
	dic = {}
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

#删除
def remove():
	name = input("请输入您要删除的名字")	
	for i in range(0,len(list)):
		if list[i] ["name"] == name:
			list.pop(i)
			break



#修改
def chage():
	name = input("请输入你要修改的名字")
	isShow = True
	for i in range(0,len(list)):
		if list[i] ["name"] == name:
			chageContent(i)
			isShow = false
			break
	else:
		if isShow:
			print("你输入的人不存在")



def changeContent(position):
	isloop = True
	while isloop:
		mode = int(input(" 请输入要输入的信息: 1.名字 2.年龄 3.性别 4.工作 5.地址 6.退出"))
		
		if mode == 1:
			name = input("请输入新的名字")
			list[position]["name"] = name
		elif mode == 2:
			age = input("请输入新的年龄") 
			list[position]["age"] = age
		elif mode == 3:
			sex = input("请输入新的性别")
			list[position]["sex"] = sex
		elif mode == 4:
			job = input("请输入新的工作")
			list[position]["job"] = job
		elif mode == 5:
			loction = input("请输入新的地址")
			list[position]["loction"] = loction
		elif mode == 6:
			isloop = Flase


#查询
def find():
	for i in list:
		print(i)



def showMenu():
	while True:
		print("欢迎进入名片管理系统".center(30,"*"))
		print("a. 新增名片".center(30,"-"))	
		print("b. 查询名片".center(30,"-"))
		print("c. 修改名片".center(30,"-"))
		print("d. 删除名片".center(30,"-"))
		print("e. 退    出".center(30,"-"))
		mode = int(input("请选择功能序号"))
		if mode == 1:
			add()
		elif mode == 2:
			find()
		elif mode == 3:
			change()
		elif mode == 4:
			remove()
		elif mode == 5:
			pass



def adminLogin():
	account = input("请输入管理员帐号:")
	pwd = input("请输入管理员密码:")
	
	
	if account != adminAcount or pwd != adminPwd:
		print("账户或密码错误")
	
	elif account == adminAccount and pwd == adminPwd:
		print("管理登录成功")
		showMenu()



adminLogin() 



