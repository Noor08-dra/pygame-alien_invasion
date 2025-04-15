class GameStats:
    def __init__(self,bg_settings):
        self.bg_settings=bg_settings
        self.reset_stats()
        self.high_score=0
        self.bg_color=(3,8,27)

    def reset_stats(self):
      # the values which have to be reset once a new game starts 
      self.ship_left= self.bg_settings.allowed_ships
      self.game_active=False
      self.score=0
      self.level=1
     