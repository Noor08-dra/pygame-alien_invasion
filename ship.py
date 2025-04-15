import pygame
from pygame.sprite import Sprite 

class Ship(Sprite):
    def __init__(self,dis_win,bg_settings):
        super(Ship,self).__init__()
        self.screen=dis_win
        self.bg_settings=bg_settings
        self.image=pygame.image.load("images/player_ship.bmp")
        self.image=pygame.transform.scale(self.image,(self.bg_settings.ship_width,self.bg_settings.ship_height))
        self.image.set_colorkey((0,255,0)) #makes the green background transparent
        self.image=self.image.convert_alpha() # maintains the transparency 
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        

        self.rect.bottom=self.screen_rect.bottom
        self.rect.centerx=self.screen_rect.centerx
         
        self.center=float(self.rect.centerx)    
         #movement flags
        self.moving_right=False
        self.moving_left=False

    def center_ship(self):
          self.center=self.screen_rect.centerx

   #Drawing the ship onto the screen
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.bg_settings.ship_speed_factor

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.bg_settings.ship_speed_factor 

        self.rect.centerx = self.center


