
sandwich_orders = ["ham sandwich","tuna sandwich","cheese sandwich"]
finished_sandwiches = []
'''
for i in sandwich_orders:
	print(i + ":" + " I made your tuna sandwich.")
'''
a = True
while a:	
	if int(len(sandwich_orders)) != 0:
		sandwich = sandwich_orders.pop()
		finished_sandwiches.insert(0,sandwich)
	else:
		a = False
print(finished_sandwiches)

print("------------------------------------------------")

print("熟食店的五香烟熏牛肉卖完啦")
sandwich_orders = ["pastrami","pastrami","pastrami","cheese"]
print(sandwich_orders)
while "pastrami" in sandwich_orders:
	sandwich_orders.remove("pastrami")
print(sandwich_orders)

print("------------------------------------------------")

name = input("请输入你的名字")
land = input("请输入你想去的地方")


