import pygame
from pygame.sprite import  Sprite
class Life(Sprite):
  def __init__(self,ai_game) -> None:
    super().__init__()
    self.screen = ai_game.screen
    self.screen_rect = self.screen.get_rect()
    self.image = pygame.image.load('graphics\life\life.png')
    self.rect = self.image.get_rect()

  def blitme(self):
    self.screen.blit(self.image , self.rect)