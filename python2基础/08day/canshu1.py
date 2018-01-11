# 20160818 有多少天
def user_print():
	
	year = int(input("请输入年份"))	
	month = int(input("请输入月份"))
	day = int(input("请输入日"))
	count_day(year,month,day)

def count_day(year,month,mDay):
	day = 0
	big_month = [1,3,5,7,8,10,12]
	small_month = [4,6,9,11]
	for i in range(1,month):
		if i in big_month:
			day += 31
		elif i in small_month:
			day += 30
		else:
			if is_leap(year):
				day += 29
			else:
				day += 28
	day += mDay
	print("第几天%d"%day)


def is_leap(year):
	if (year%4 == 0 and year%100 != 0) or year%400 == 0:
		return 1
	else:
		return 0

user_print()
