import pygame.font
from pygame.sprite import Group
from life_sprite import Life

class Scoreboard:
 
 def __init__(self, ai_game):
  self.game_active = ai_game.game_active
  self.ai_game = ai_game
  self.screen = ai_game.screen
  self.screen_rect = self.screen.get_rect()
  self.settings = ai_game.settings
  self.stats = ai_game.stats
         
  self.text_color = (255, 255, 255)
  self.leve_color = (37, 250, 17)
  self.font = pygame.font.Font('graphics\\font\Pixeltype.ttf', 48)
  
  self.prep_score()
  self.prep_high_score()
  self.perp_level()
  self.prep_life()
  self.save_highescore()


 def prep_score(self):
  round_score = round(self.stats.score , -1)
  score_str = f'{round_score:,}'
  self.score_image = self.font.render(score_str, True,
  self.text_color)

  self.score_rect = self.score_image.get_rect()
  self.score_rect.right = self.screen_rect.right - 20
  self.score_rect.top = 20

 
 def prep_high_score(self):
  high_score = round(self.stats.high_score, -1)
  high_score_str = f"{high_score:,}"
  self.high_score_image = self.font.render(high_score_str, True,
  self.text_color)

  self.high_score_rect = self.high_score_image.get_rect()
  self.high_score_rect.centerx = self.screen_rect.centerx
  self.high_score_rect.top = self.score_rect.top
 
 
 def perp_level(self):
  level_str = str(self.stats.level)
  self.level_image = self.font.render(level_str , True , self.leve_color)

  self.level_rect  = self.level_image.get_rect()
  self.level_rect.right = self.score_rect.right
  self.level_rect.top = self.score_rect.bottom + 15


 def prep_life(self):
  self.life = Group()
  for life_num in range(self.stats.ship_left):
   life = Life(self.ai_game)
   life.rect.x = 10 + life_num * life.rect.width
   life.rect.y = 10
   self.life.add(life)

 def show_score(self):
   self.screen.blit(self.score_image, self.score_rect)
   self.screen.blit(self.high_score_image, self.high_score_rect)
   self.screen.blit(self.level_image, self.level_rect)
   self.life.draw(self.screen)
   self.screen.blit(self.saved_image , self.saved_image_rect)

 
 def save_highescore(self):
  num = self.stats.high_score
  if self.stats.high_score != 0:
    file = open('score.txt','r')
    for saved in file:
      if int(saved) < self.stats.high_score:
        num = self.stats.high_score
        num_str = str(num)
    file.close()
    text = open('score.txt','w')
    text.write(str(num)+'\n')
    text.close()


 def find_largest_num(self):
  largest_num = 0
  f = open('score.txt','r')
  largest_num = int(f.readline())
  f.close()  
  self.saved_image = self.font.render(str(largest_num) , True , self.text_color)
  self.saved_image_rect = self.saved_image.get_rect()
  self.saved_image_rect.left = 50
  self.saved_image_rect.top = 70

 def check_high_score(self):
   if self.stats.score > self.stats.high_score:
    self.stats.high_score = self.stats.score
    self.prep_high_score()
