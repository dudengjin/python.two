# 嘉宾名单
list = ["liutingting","fenxinming","duanjinsong"]
print(list)

print("----------------分割线-----------------")

print(list[2] + "cant come this party")
list[2] = "dudengjin"
print(list)

print("-----------------分割线-------------------")

print("I found a bigger table.")
list.insert(0,"wanghanqing")
print(list)
list.insert(2,"wangxiliang")
print(list)
list.append("menweijia")
print(list)

print("-----------------分割线------------------")
print("I am sorry about that only two guests can come this party")
for n in range(0,4):
	num = 1
	num += 1
	leave = list.pop(num)
	print(leave + "I'm sorry I can't invite him to dinner.")
for n in range(0,2):
	print("congratulation "+list[0]+" you can come party")
	del list[0]
print(list)





