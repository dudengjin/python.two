st =[{"beijing":{"mianji":1290,"renkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]


for i in st:
	print(i)
	for i,j in st:
		print(i,j)
		for key in i,j:
			print(key,(i,j)[key])	
	
