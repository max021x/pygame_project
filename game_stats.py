import pygame.font

class GameStats:
  def __init__(self , ai_game) -> None:
    self.settings = ai_game.settings
    self.screen = ai_game.screen
    self.screen_rect = self.screen.get_rect()
    self.reset_stats()
    self.high_score = 0
    self.level = 1 
  def reset_stats(self):
    self.ship_left = self.settings.ship_limit
    self.score = 0
    self.level = 1
 
  


