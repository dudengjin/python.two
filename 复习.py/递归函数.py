num = 4
def calNum1(num=4):
	if num > 1:
		return num*calNum1(4-1)
	else:
		return num

		4*返回值


def calNum1(num=3):
	num*calNum(3-1)


		3*返回值


def calNum1(num=2):
	num*calNum(2-1)

		2*返回值


def calNum1(num=1):
	num*calNum(1-1)

		1*返回值 

