'''
for i in range(1,21):
	print(i)


number = list(range(1,1001))
print(number)


number = list(range(1,1000001))  
print(min(number))  
print(max(number))  
print(sum(number))  


number = list(range(1,20,2))
for i in number:
	print(i)


number = list(range(3,31))
number1 = []
for i in number:
	if i %3 == 0:
		number1.append(i)
print(number1)


'''
num = list(range(1,11,1))
num1 = []
for i in num:
	i = i ** 2
	num1.append(i)
print(num1)



list = [valce**3 for valce in range(1,11)]
print(list)



