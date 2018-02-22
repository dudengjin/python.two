python = {'bool':'布尔','str':'字符串','int':'整数','list':'列表','tuple':'元组'}
for k,v in python.items():
	print(k,v)

print("--------------------------------------")

dic = {'nile':'egypt','MeKong':'qinghai','Danube':'Germany'}
# 尼罗河，埃及，眉公河，青海，多瑙河，德国
for k,v in dic.items():
	print('The ' + k + ' runs through ' + v + '.')

print("--------------------------------------")

for k in dic.keys():
	print('This river is called ' + k)

print("--------------------------------------")

for v in dic.values():
	print('state: ' + v)

print("--------------------------------------")

people = {'jen':'python','sarch':'c','edward':'ruby','phil':'python'}
for k in people.keys():
	print(k + ' Thank you for your inquiry.') # 谢谢你接受调
	
print("--------------------------------------")

people = {'jen':'python','sarch':'c','edward':'ruby','phil':'python'}
if 'Eric' not in people.keys():
	print("Eric,Please accept the survey")
