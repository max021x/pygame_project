import pygame
import random 
from pygame.sprite import Sprite

class Alien(Sprite):
  def __init__(self, ai_game) -> None:
    super().__init__()
    self.screen = ai_game.screen
    self.screen_rect = self.screen.get_rect()
    self.settings = ai_game.settings

    self.image = pygame.image.load('graphics\\alien\\alien.png')
    self.rect = self.image.get_rect()
    self.rect.y = -1* (random.randint(100,550))
    self.rect.x = random.randint(0,1000) 

    self.y = float(self.rect.y)

  def update(self):
    self.y += self.settings.alien_speed
    self.rect.y = self.y

  
    