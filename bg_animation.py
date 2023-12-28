import pygame

class Background:
  def __init__(self , ai_game) -> None:
    self.screen = ai_game.screen
    self.screen_rect = self.screen.get_rect()
    self.image_1 = pygame.image.load('graphics\space_bg\\bg (1).jpg')
    self.image_2 = pygame.image.load('graphics\space_bg\\bg (2).jpg')
    self.image_3 = pygame.image.load('graphics\space_bg\\bg (3).jpg')
    self.image_4 = pygame.image.load('graphics\space_bg\\bg (4).jpg')
    self.image_5 = pygame.image.load('graphics\space_bg\\bg (5).jpg')
    self.image_6 = pygame.image.load('graphics\space_bg\\bg (6).jpg')
    self.image_7 = pygame.image.load('graphics\space_bg\\bg (7).jpg')
    self.image_8 = pygame.image.load('graphics\space_bg\\bg (8).jpg')
    self.image_9 = pygame.image.load('graphics\space_bg\\bg (9).jpg')
    self.image_10 = pygame.image.load('graphics\space_bg\\bg (10).jpg')
    self.image_11 = pygame.image.load('graphics\space_bg\\bg (11).jpg')
    self.image_12 = pygame.image.load('graphics\space_bg\\bg (12).jpg')
    self.image_13 = pygame.image.load('graphics\space_bg\\bg (13).jpg')
    
    self.img_list = [self.image_1, self.image_2, self.image_3 , self.image_4, self.image_5 , self.image_6, self.image_7,self.image_8,self.image_9,self.image_10,self.image_11,self.image_12,self.image_13]
    self.image_indext = 0
    self.image_surf = self.img_list[self.image_indext]
    self.image_rect = self.image_surf.get_rect()
    self.image_rect.center = self.screen_rect.center
    self.animation()
  
  def animation(self):

    self.image_indext += 0.2
    if self.image_indext >= len(self.img_list):self.image_indext = 0
    self.image_surf = self.img_list[int(self.image_indext)]

  def blit(self):
    self.screen.blit(self.image_surf , self.image_rect)
    
  