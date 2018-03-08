class MusicPlayer(object):
	
	ice = None
	def __new__(cls):
		if cls.ice is None:
			cls.ice = super().__new__(cls)
		return cls.ice	

	def __init__(self):
		print("连借口都没有")	


V = MusicPlayer()
V1 = MusicPlayer()
print(V) 
print(V1)