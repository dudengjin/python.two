car = 'bmw'  
cars = ['bmw','audi']  
#T  
print(car == 'bmw')  
#F  
print(car != 'bmw')  
#T  
print(car == car)  
#F  
print(car == car.title())  
#T  
print(car == 'bmw' or  car == 'audi')  
#F  
print(car == 'bmw' and car == 'audi')  
#T  
print(int(len(car)) == int(len('bmw')))  
#F  
print(int(len(car)) == int(len('audi')))  
#T  
print('bmw' in cars)  
#F  
print('audi' not in cars)  

print("-----------------分割线------------------")	


water = ["black tea","green tea","milky tea","cheese"]
for i in water:
	print(i)
	if i == "cheese":
		print("welcome to taste") # 欢迎品尝
	else:
		print("Please reselect") # 请重新挑选

print("-----------------分割线------------------")	

water = ["black tea","green tea","milky tea","cheese"]
for i in water:
	print(i)
	
	if i == "green tea":
		print(True)
	else:
		print(False)

print("-----------------分割线------------------")	

car = ["baoma","banchi","luhu","beijingxiandai",]
for i in car:
	print(i)
	if car == "qiche":
		print(True)
	else:
		print(False)




