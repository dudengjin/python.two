
number = 2
while number <= 100:
	if number%2 != 0 and number%3 != 0 and number%5 != 0 and number%7 != 0:
		print(number)
	number += 1




for i in range(2,100):
	
	fn =0
	for j in range(2,i):
		if i%j == 0:
			fn = 1
			break
	if fn == 0:
		print(i)	










'''
for i in range(1,10):
	for j in range(1,i+1):
		print("%d*%d=%d"%(j,i,j*i),end ="\t")
	print("")
'''
