import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
      def __init__(self,screen,bg_settings):
            super(Alien,self).__init__()
            self.screen=screen
            self.screen_rect=self.screen.get_rect()
            self.settings=bg_settings
            
            self.image=pygame.image.load("images/alien.bmp")
            self.image=pygame.transform.scale(self.image,(self.settings.alien_width,self.settings.alien_height))
            self.image.set_colorkey((0,255,0)) #makes the green background transparent
            self.image=self.image.convert_alpha() # maintains the transparency
            self.rect=self.image.get_rect()

            self.rect.topleft=(self.settings.start_x,self.settings.start_y)

            self.x=float(self.rect.x)
            self.y=float(self.rect.y)
     
      def blitme(self):
          self.screen.blit(self.image,self.rect)
      
      def update(self):
           self.x+=self.settings.fleet_moving_factor*self.settings.fleet_direction
           self.rect.x=self.x
           
      def check_edges(self):
           if self.rect.right>=self.screen_rect.right:
                return True 
           elif self.rect.left<=0:
                return True

                