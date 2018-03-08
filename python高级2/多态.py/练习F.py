class Animal(object):
	
	def __init__(self,name):
		self.name = name

	def Game(self):
		print("%s在踢球"%self.name)

class tiger(Animal):

	def Game(self):
		print("%在草地踢球"%self.name)

class cat(object):

	def __init__(self,name):
		self.name = name

	def Game_cat(self,z):
		print("%s和%s在草地踢球"%(self.name,z.name))	

boluo = Animal("菠萝")
boluo.Game()
lizhi = cat("荔枝")
lizhi.Game_cat(boluo)
