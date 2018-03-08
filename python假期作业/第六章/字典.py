message = {'first_name':'dengjin','last_name':'du','city':'taiyuan'}
print(message['first_name'])
print(message['last_name'])
print(message['city'])

print("---------------------------------------")

for k,v in message.items():
	print(k,v)

print("---------------------------------------")

number = {'du':'2','li':'3','wang':'4','fen':'5','huo':'6'}
print(number)

print("---------------------------------------")

for k,v in number.items():
	print(k,v)

print("---------------------------------------")

python = {'bool':'布尔值','str':'字符串','int':'整数','list':'列表','tuple':'元组'}
for k,v in python.items():
	print(k,v)

print("---------------------------------------")

python = {'bool':'布尔值','str':'字符串','int':'整数','list':'列表','tuple':'元组'}
for k,v in python.items():
	print(k + ':'+ v)


