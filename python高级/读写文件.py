#打开一个已经存在的文件

f = open('text.txt','r')
str = f.read()
print(str) # 读取数据


# 查找当前位置
position = f.tell()
print(position) # 当前位置



# 重新设置位置
f.seek(5,0)

f.close()



import os
os.rename()  # 需要修改的文件名, 新文件名

os.remove()  # 待删除的文件名

