for i in range(101,201):
	k = 0 
	for a in range(2,i):
		if i % a == 0:
			k += 1
	if k == 0:
		print(i)




count = 0
while count <= 5:
	kongge = 0
	while kongge < 5-count:
		print(end=" ")
		kongge += 1	
	
	star = 0 
	while star < count:
		print("*",end=" ")
		star += 1
	print("")						
	count += 1