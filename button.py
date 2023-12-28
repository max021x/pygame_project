import pygame

class Button:
  def __init__(self , ai_game , msg) -> None:

    self.screen = ai_game.screen
    self.settings = ai_game.settings
    self.screen_rect = self.screen.get_rect()
    
    self.width, self.height = 150, 50
    self.button_color = (0, 135, 0)
    self.text_color = (255, 255, 255)
    self.game_over_color = (245, 66, 108)
    self.font = pygame.font.Font('graphics\\font\Pixeltype.ttf', 53)
    self.over_font = pygame.font.Font('graphics\\font\Pixeltype.ttf' , 200)
    self.rect = pygame.Rect(0, 0, self.width, self.height)
    self.rect.center = self.screen_rect.center

    self._prep_msg(msg)
    self.game_over()

  def _prep_msg(self, msg):
    self.msg_image = self.font.render(msg , False , self.text_color , self.button_color)
    self.msg_image_rect = self.msg_image.get_rect()
    self.msg_image_rect.center = self.screen_rect.center
    self.msg_image_rect.y += 5


  def game_over(self):
   self.show_msg = self.over_font.render('Game over' , True , self.game_over_color)
   self.show_msg_rect = self.show_msg.get_rect()
   self.show_msg_rect.center = self.screen_rect.center  
  
  def draw_button(self):
      if self.settings.ship_limit > -1:
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
      else:
        self.screen.blit(self.show_msg , self.show_msg_rect)

