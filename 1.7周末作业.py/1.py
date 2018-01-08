
for i in range(1,5000,1):
	if (i%5 == 0 and i%7 ==0):
		print(i)





count = 1
while count <= 5000:
	if count%5 == 0 and count%7 == 0:
		print(count)
	count += 1








'''
import random

count = 1
while count <= 10:
	
	computer = random.randint(1,100)  # 电脑玩家
	number = int(input("请输入一个数字"))
	
	if number < computer:
		print("猜小")
	elif number > computer:
		print("猜大")
	elif number == computer:
		print("猜中")
		break
	
	count += 1





import random
# 电脑随机出来的数

computer = random.randint(1,101)
for i in range(1,11):	
	number = int(input("请输入一个数字"))
	if number > computer:
		print("猜小")
	elif number == computer:
		print("猜中")
		break
	else:
		print("猜大")
'''	
