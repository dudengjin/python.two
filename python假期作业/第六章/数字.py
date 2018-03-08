number = {'du':'2','li':'3','wang':'4','fen':'5','huo':'6'}
for k,v in number.items():
	print(k,v)

print("-------------------------------------------")

cities = {'beijing':{'country:Chinese','population:500','fact:国际大都市'},'shanghai':{'country:Chinese','population:1000','fact:首批沿海开放城市'},'taiwan':{'country:Chinese','population:300','fact:中国第一大岛'}}
for city,mess in cities.items():
	print(city,mess)
	
	for i in mess:
		print(i)






