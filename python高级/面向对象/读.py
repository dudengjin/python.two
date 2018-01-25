# r  只读方式
# w  写    存在回覆盖，不存在，新建文件
# a  追加  新内容会追加到已有内容之后
# rb  二进制格式打开

# 创建一个文件 打开 
f = open('test.txt','w') 


f.close()
# 关闭




f = open('test.txt','w')

f.write('hello world') # 写入数据
f.close()





# 读取数据
f = open('test.txt','r')
content = f.read()
 
content = f.readlines()
print(type(content))


print(content)
f.close()


