class Settings:
  def __init__(self) -> None:
    # screen settings
    self.screen_width = 1100
    self.screen_hieght = 870
    self.bg_color =(230,230,230)

    # ship settings
    # self.ship_speed = 5
    self.ship_limit = 3
    
    # bullet settings
    # self.bullet_speed = 2
    self.bullet_width = 3
    self.bullet_hieght = 15
    self.bullet_color = (252, 3, 3)
    self.bullet_allowed = 3

    # alien settings 
    # self.alien_speed = 1

    # game speed scale 
    self.speedup_scale = 1.1
    self.score_scale = 1.2

    self.initialize_dynaminc_setting()
  
  def initialize_dynaminc_setting(self):
    self.ship_speed = 5
    self.bullet_speed = 3
    self.alien_speed = 1
    self.alien_point = 50

  def increase_speed(self):
    self.ship_speed *= self.speedup_scale
    self.alien_speed *= self.speedup_scale
    self.bullet_speed *= self.speedup_scale
    self.alien_point = int(self.score_scale * self.alien_point)