
car = input("请输入您要租赁的汽车")
print("Let me see if I can find you a Subaru. " + car)

print("-----------------------------------")

eat = int(input("请输入用餐人数"))
if eat >= 8:
	print("不好意思,没有空座位啦")
else:
	print("有座位哦")

print("-----------------------------------")

use = int(input("请输入一个数字"))
if use % 10 == 0:
	print("是10的整数倍")
else:
	print("不是10的整数倍")
