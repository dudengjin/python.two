
Add = ["apple","dragon fruit","luckly","admin","monday"]
for i in Add:
	if i == "admin":
		print("Hello admin,would you like to see a stuuts report?")
	else:
		print("Hello Eric,thank you for logging in again.")

print("-----------------分割线---------------")

Adds = []
Add = ["apple","dragon fruit","luckly","admin","monday"]
if Add not in Adds:
	print("We need to find some users")
for i in Add:
	if i == "admin":
		print("Hello admin,would you like to see a stuuts report?")
	else:
		print("Hello Eric,thank you for logging in again.")

print("-----------------分割线---------------")

current_users = ["apple","dragon fruit","luckly","admin","monday"]
new_users = ["pear","cherry","admin","luckly","monday"]
for i in new_users:
	i = i.lower()
	if i in current_users:
		print("sorry,您需要输入别的用户名")
	else:
		print("用户名未使用")

print("-----------------分割线---------------")

numbers = list(range(1,10))
for list in numbers:
	if list == 1:
		print("1st")
	elif list == 2:
		print("2nd")
	elif list == 3:
		print("3rd")
	else:
		print("str(list) + th")



