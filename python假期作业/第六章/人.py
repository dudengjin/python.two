
message = {'first_name':'dengjin','last_name':'du','city':'taiyuan'}
messageA = {'first_name':'tingting','last_name':'liu','city':'datong'}
messageB = {'first_name':'xingming','last_name':'fen','city':'yuncheng'}
People = [message,messageA,messageB]
print(People)
for i in People:
	print(i)
	for k,v in i.items():
		print(k + ':' +  v)

print("------------------------------------------")

dog = {'type':'松狮','master name':'dudengjin'}
dog1 = {'type':'博美','master name':'liu'}
dog2 = {'type':'约克夏','master name':'huo'}
pets = [dog,dog1,dog2]
for i in pets:
	print(i)
	for k,v in i.items():
		print(k + ':' +  v)

print("------------------------------------------")

favorite_places = {'dudengjin':'taiwan,shanghai','huotong':'taiyuan,','liutingting':'beijing,datong'}
for places in favorite_places.items():
	print(places)
	for i in places:
		print(i)



