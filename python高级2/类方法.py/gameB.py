class Game(object):
	# 类属性
	top_score = 99
	# 静态方法
	@staticmethod
	def show_help():
		print("欢迎进入到我的世界")
	# 类方法
	@classmethod
	def show_top_score(cls):
		print("最高分是:"+ str(cls.top_score)	)

	def __init__(self,name):
		self.player_name = name	

	def star_game(self):
		print("开始游戏")	

xiao_xiao = Game("小小")

Game.show_top_score()
Game.show_help()