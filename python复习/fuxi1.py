# ATM取款系统

account = input("请输入帐号")
pwd = input("请输入密码")
name = input("请输入姓名")
money = 30000  #原有的金额
take_money = input("请输入要取的金额")
sum = money - int(take_money)

print("帐号:%s"%account)
print("密码:%s"%pwd)
print("姓名:%s"%name)
print("原有金额:%s"%money)
print("要取的金额:%s"%take_money)
print("余额为:%s"%sum)

'''
print("帐号:%s\n 密码×××××\n 姓名:%s\n 原有存款为%d\n 取款金额为%s\n  剩余%d"%(account,name,money,take_money,sum))
'''



