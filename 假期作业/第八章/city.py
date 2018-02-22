
def city_country(city_name,country):
	c_country = city_name +' ' + country
	return c_country

city = city_country('Santiago','chile')
cityA = city_country('shanghai','Chinese')
cityB = city_country('Barcelona','Spain') # 巴塞隆纳, 西班牙 
print(city)
print(cityA)
print(cityB)

print("-------------------------------------")

def make_album(Artist,album,song_num = ''): 
	if song_num:
		ge = {'Arist':Artist,'album':album,'song_num':song_num}
	else:
		ge = {'Arist':Artist,'album':album}
	return ge

singer = make_album('简弘亦','出卖')
singerA = make_album('余佳运','不露声色')
singerB = make_album('何以爱情','钟汉良')
print(singer)
print(singerA)
print(singerB)

print("-------------------------------------")	

def make_album(Artist,album,song_num = ''): 
	if song_num:
		ge = {'Arist':Artist,'album':album,'song_num':song_num}
	else:
		ge = {'Arist':Artist,'album':album}
	return ge

Arist = input("请输入你的歌手名")
album = input("请输入你的专辑名")

while True:
	ge = input(Arist)
	shou = input(album)
	if ge == 'q' or shou == 'q':
		break
	else:
		singer = make_album(ge,shou)
		print(singer)







