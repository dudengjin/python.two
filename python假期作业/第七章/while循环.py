
while True:
	pizza = input("请输入你选项的配料")

	if  'quit'in pizza:
		break
	else:
		print("我们会在比萨中添加配料:" + pizza )
		
print("---------------------------------------")

while True:
	age = int(input("请输入年龄"))
	
	if'quit'in age:
		break
	elif age <= 3:
		print("免费")
	elif 3 <= age <=12:
		print("10美元")
	elif age >= 12:
		print("15美元")

print("---------------------------------------")

'''
# 无限循环
name = input("请输入你的名字")	
while True:
	print(name)
'''

