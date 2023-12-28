import pygame
import sys
import random
from time import sleep
from button import Button
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from scored import Scoreboard
from bg_animation import Background
from music import Music
pygame.init()

class Alien_Game:
  def __init__(self) -> None:
    self.settings = Settings()
    self.screen = pygame.display.set_mode([self.settings.screen_width , self.settings.screen_hieght])
    self.clock = pygame.time.Clock()
    self.bg = Background(self)
    self.ship = Ship(self)
    self.bullet =  pygame.sprite.Group()
    self.alien = pygame.sprite.Group()
    self.stats = GameStats(self)
    self.game_active = False
    self.play_button = Button(self,'PLAY')
    self.sb = Scoreboard(self)
    self.bg_sound = Music()
    self.random_alien = random.randint(3,25)
    self.create_fleet(self.random_alien)

  def run_game(self):
    while True:
      self.check_event()
      
      if self.game_active:
        self.ship.update_ship()
        self.bullet_update()
        self.update_aliens()
      if not self.game_active:
        self.sb.save_highescore()
        self.sb.find_largest_num()
      self.update_screen()
      self.clock.tick(60)
  
  def check_event(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        # self.sb.saved_highescore()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._key_down(event)
      elif event.type == pygame.KEYUP:
        self._key_up(event)
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        self.check_play_button (mouse_pos)
  

  def update_screen(self):
    self.bg.blit()
    self.bg.animation()
    self.ship.blitme()
    for bullet in self.bullet.sprites():
        bullet.draw_bullet()
    self.alien.draw(self.screen)
    self.sb.show_score()

    if not self.game_active:
      pygame.mouse.set_visible(True)
      self.play_button.draw_button()
      
    
    pygame.display.flip()
    

  def _key_down(self, event):
    if event.key  == pygame.K_RIGHT:
      self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = True
    elif event.key == pygame.K_q:
      sys.exit()
    elif event.key == pygame.K_SPACE:
      self.fire_bullet()
      self.bg_sound.balzer_play()
    elif event.key == pygame.K_r and self.settings.ship_limit < 0:
      self.game_active = True
      self.settings.ship_limit = 4

  def _key_up(self , event): 
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = False
  
  def fire_bullet(self):
      newbullet = Bullet(self)
      self.bullet.add(newbullet)

  def bullet_update(self):
    self.bullet.update()
    for bullet in self.bullet.copy():
      if bullet.rect.bottom <= 0:
        self.bullet.remove(bullet)
 
    self._check_bullet_alien_collisions()

  def _check_bullet_alien_collisions(self):
    
    colisions = pygame.sprite.groupcollide(self.alien , self.bullet , True , True)
  
    if not self.alien:
      self.random_alien = random.randint(10,30)
      self.create_fleet(self.random_alien)
      self.settings.increase_speed()
      self.stats.level +=1
      self.sb.perp_level()
    
    if colisions :
      self.bg_sound.expolosion_play()
      for aliens in colisions.values():
        self.stats.score += self.settings.alien_point * len(aliens)
      self.sb.prep_score()
      self.sb.check_high_score()
     
  def create_fleet(self , random):
   while len(self.alien) < random:
      alien = Alien(self)
      if not pygame.sprite.spritecollide(alien , self.alien , False):
        self.alien.add(alien)

  def update_aliens(self):
    self.alien.update()
    if pygame.sprite.spritecollideany(self.ship , self.alien):
      self._ship_hit()
    self._check_alien_bottom() 

  def _ship_hit(self):
    self.settings.ship_limit -=1
    self.bg_sound.stop_sound()
    self.bg_sound.game_over_play()
    
    if self.stats.ship_left < 0:
      self.random_alien = random.randint(15,25)
      self.sb.prep_life()
      self.bullet.empty()
      self.alien.empty()
      self.create_fleet(self.random_alien)
      self.ship.center_ship()

      sleep(0.5)
    
    elif self.settings.ship_limit < 0:

      self.game_active = False
    
    else :
      self.game_active = False

  def _check_alien_bottom(self):
    for alien in self.alien.sprites():
      if alien.rect.bottom >= self.settings.screen_hieght:
        self._ship_hit()
        break

  def check_play_button(self , mouse_pos):
      button_clicked = self.play_button.rect.collidepoint(mouse_pos)
      if button_clicked and not self.game_active:
        pygame.mouse.set_visible(False)
        self.settings.initialize_dynaminc_setting()
        self.stats.reset_stats()
        self.sb.prep_score()
        self.sb.perp_level()
        self.sb.prep_life()
        self.random_alien = random.randint(15,25)

        self.game_active = True
        self.bg_sound.play_sound()

        self.alien.empty()
        self.bullet.empty()

        self.create_fleet(self.random_alien)
        self.ship.center_ship()


ai_game = Alien_Game()
ai_game.run_game()
