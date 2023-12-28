import pygame

class Music:
  def __init__(self) -> None:
    self.bg_sound_ = pygame.mixer.Sound('graphics\sound\Space Heroes.ogg')
    self.balzer_sound = pygame.mixer.Sound('graphics\sound\\blaster-2-81267.mp3')
    self.expolosion = pygame.mixer.Sound('graphics\sound\8-bit-cannon-fire-96505.mp3')
    self.game_over = pygame.mixer.Sound('graphics\sound\\videogame-death-sound-43894.mp3')

  def play_sound(self):
    self.bg_sound_.play()
  
  def stop_sound(self):
    self.bg_sound_.stop()

  def balzer_play(self):
    self.balzer_sound.play()
  
  def expolosion_play(self):
    self.expolosion.play()
  
  def game_over_play(self):
    self.game_over.play()