
list = ["0","1","2","3","4","5","6","7"]
print("The first three items in the list are") 
list1 = list[0:3]
for i in list1:
	print(i)


print("The items from the middle of the list are")
for i in list[3:6]:
	print(i)


print("The last three items in the list are")
for i in list[-3:]:
	print(i)


print("-----------------分割线-------------------")

Pizza = ["田园比萨","夏威夷比萨","奥尔良比萨"]

friend_pizzas = Pizza[:]
Pizza.append("什锦比萨")
friend_pizzas.append("水果比萨")
print(Pizza)
print(friend_pizzas)


print("My favorite pizzas are:")
print(Pizza)
for i in Pizza:
	print(i)

print("My friend's favorite pizzas are:")
print(friend_pizzas)
for i in friend_pizzas:
	print(i)


print("-----------------分割线-------------------")


food = ["chicken","hamburger","chips","noodle",]
for i in food:
	print(i)






