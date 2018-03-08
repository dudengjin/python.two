class MusicPlayer(object):
	def __new__(cls,*a,**b):
		
		print("new方法")
		# 分配内存空间
		return super().__new__(cls)

	def __init__(self):
		print("init方法")

a = MusicPlayer()
