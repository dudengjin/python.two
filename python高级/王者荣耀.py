print('欢迎来到召唤师峡谷!')


frist_name = 'du'
last_name = 'dengjin'
full_name = frist_name + last_name
print(full_name)
print('尊敬的召唤师:欢迎来到召唤师峡谷!')

heroes =['兰陵王','安吉拉','李白','貂蝉','孙悟空','鲁班','妲己', '后裔']
print(heroes)

print(heroes[0])
print(heroes[1])

heroes.append('兰陵王')

heroes.insert(0,'兰陵王')


del heroes[0]


tail = heroes.pop()
print(heroes)
print(tail)

heroes.remove('后裔')


heroes =['安吉拉','李白','貂蝉','孙悟空','鲁班','妲己']
heroes.sort()
print(heroes)

heroes.sort(reverse=True)
print(heroes)

# 反向排列
heroes.reverse()
print(heroes)

for hero in heroes:
	if hero == '李白':
		print('你选的英雄超级厉害的!')
	else:
		print('你选的英雄一般!')





