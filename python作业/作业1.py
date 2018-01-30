class User(object):
	def __init__(self):
		self.__frist_name = frist_name 
		self.__last_name = last_name
		self.__addr = addr
	
	def getFrist_name(self):
		return self.__frist_name

	def getLast_name(self):
		return self.__last_name

	def getAddr(self):
		return self.__addr

	def setFrist_name(self,newfrist_name):
		self.__frist_name = newfrist_name
		return self.__frist_name

	def setLast_name(self,newlast_name):
		self.__last_name = newlast_name
		return self.__last_name

	def setAddr(self,newaddr):
		self.__addr = newaddr
		return self.__addr


	def describe_User(self):
		print(self.frist_name)
		print(self.last_name)

	def greet_user(self):
		print('%s%s说:你好!'%self.__frist_name,__last_name)


a = User
a.selffrist_name('杜登进')
a.selflast_name('杜')
a.selfaddr('山西')

