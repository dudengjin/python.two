age = int(input("请输入你的年龄"))
if age < 2:
	print("婴儿")
elif 2 <= age < 4:
	print("蹒跚学步")
elif 4 <= age < 13:
	print("儿童")
elif 13 <= age < 20:
	print("青少年")
elif 20 <= age < 65:
	print("成年人")
else:
	print("老年人")

print("--------------分割线---------------")

fruit = ["apple","banana","orange",]
if "apple"in fruit:
	print("You really like apple")
if "banana"in fruit:
	print("You really like banana")
if "orange"in fruit:
	print("You really like orange")
