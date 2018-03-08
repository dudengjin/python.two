
def sandwich_eat(*food):
	print("你需要的食材有:")
	for i in food:
		print(i)

sandwich_eat('egg','bread','lettuce','salad')
sandwich_eat('egg')
sandwich_eat('egg','bread')

print("-----------------------------------------")

def build_profile(first, last, **user_info):    

	profile = {}
	profile['first_name'] = first 
	profile['last_name'] = last 
	
	for k,v in user_info.items():
		profile[k] = v    
	return profile 

user = build_profile('albert', 'einstein',  location='princeton',  field='physics') 
print(user)
userA = build_profile('albert', 'einstein',field='physics') 
print(userA)

print("-----------------------------------------")

def car_message(car_name,car_trait,**car):
	car_m = {}
	car_m['name'] = car_name
	car_m['trait'] = car_trait
	
	for k,v in car.items():
		car_m[k] = v
	return car_m

car = car_message('subaru','outback',color='blue',tow_package=True) 
print(car)



