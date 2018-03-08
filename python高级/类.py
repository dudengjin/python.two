class Person(object):
	
	def __init__(self,eye):
		self.eye = eye
		
	def walk(self):
		print("人在走")

	def __str__(self):
		return"我爱你"

duan_jin_song = Person("white")
duan_jin_song.walk



