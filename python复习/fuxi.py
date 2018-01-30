
name = input("请输入姓名")
print("我的名字叫:%s, 请多多关照!"%name)

student_no = int(input("请输入学号"))
print("我的学号是:%06d"%student_no)


price = float(input("请输入价格"))
weight = float(input("请输入重量"))
money = price*weight
print("西瓜单价%.02f元/斤，购买%.02f斤，需要支付%.02f元."%(price,weight,money))


scale = float(input("请输入数据"))
print("数据比列是%.02f%%"%(scale*1))



name = input("请输入姓名")
company = input("请输入公司")
position = input("请输入职位")
tel = input("请输入电话")
email = input("请输入电子邮件")

print("我的名字叫:%s"%name)
print("我在:%s公司"%company)
print("职位是:%s"%position)
print("电话:%s"%tel)
print("电子邮件:%s"%email)




y = 365
d = 24
h = 60
m = 60
m = y*d*h*m
print(m)


km = 1000
m = 100
cm = 100
mm = km*m*cm
print(mm)


x = 2
print(6*(x/7))
print(6/(4+5*x))


