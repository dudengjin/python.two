# 求1～100的和
def print_he():
	sum1 = 0#这是奇数和
	sum2 = 0#这是偶数和
	sum3 = 0#这是总和
	
	for i in range (1,101):
		if i%2 != 0:
			sum1 = sum1 + i
		if i%2 == 0:
			sum2 = sum2 + i

		sum3 = sum2 + sum1
	
	print(sum1)
	print(sum2)
	print(sum3)

print_he()









