import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen,ship,bg_settings):
        super().__init__()
        self.screen=screen
        self.ship=ship
        self.bg_settings=bg_settings
        
        self.rect=pygame.Rect((0,0,self.bg_settings.bullet_width,self.bg_settings.bullet_height))
        self.image=pygame.Surface((self.bg_settings.bullet_width,self.bg_settings.bullet_height))
        self.image.fill((self.bg_settings.bullet_color))
    
       #position of the bullet
        self.rect.centerx=self.ship.rect.centerx
        self.rect.top=self.ship.rect.top

        self.rect.y=float(self.rect.top)

    def draw(self):
       self.screen.blit(self.image,self.rect)  
    
    def update(self):
    
        self.rect.y -= self.bg_settings.bullet_speed_factor
        self.rect.top=self.rect.y

    