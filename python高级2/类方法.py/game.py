class Game(object):
	top_score = 99

	@staticmethod
	def show_help():
		print("帮助信息:让僵尸走进房间")

	@classmethod
	def show_top_score(cls):
		print("游戏最高分是%d"%cls.top_score)

	def __init__(self,player_name):
		self.player_name = player_name

	def start_game(self,name):
		print("开始游戏"%self.player_name)

Game.show_help()
Game.show_top_score()

game = Game("小明")
Game.show_help()
Game.show_top_score()
