import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    def __init__(self,screen,bg_settings,stats):
        self.screen=screen
        self.settings=bg_settings
        self.stats=stats

        self.bg_color=self.stats.bg_color
        self.text_color=(0,255,0)
        self.font=pygame.font.SysFont(None,48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        self.rounded_score=int(round(self.stats.score,-1)) #rounding off the score to nearest multiple of 10
        self.score_str="{:,}".format(self.rounded_score) #including thousands separator in large numbers 
        self.score_image=self.font.render(self.score_str,True,self.text_color,self.bg_color)
        self.score_image.set_colorkey((self.bg_color))
        self.score_rect=self.score_image.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20
        

    def prep_high_score(self):
        self.high_score=int(round(self.stats.high_score,-1)) #rounding off the hight score to nearest multiple of 10
        self.high_score_str="{:,}".format(self.high_score) #including thousands separator in large numbers 
        self.high_score_image=self.font.render(self.high_score_str,True,self.text_color,self.bg_color)
        self.high_score_image.set_colorkey((self.bg_color))
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=20


    def prep_level(self):
        self.level=str(self.stats.level)
        self.level_image=self.font.render(self.level,True,self.text_color,self.bg_color)
        self.level_image.set_colorkey((self.bg_color))
        self.level_image_rect=self.level_image.get_rect()
        self.level_image_rect.right=self.score_rect.right
        self.level_image_rect.bottom=self.score_rect.bottom+40
              
    def prep_ships(self):
        # see how many ships are left 
        self.ships=Group()
        for ship_num in range(self.stats.ship_left):
            ship=Ship(self.screen,self.settings)
            ship.image=pygame.transform.scale(ship.image,(self.settings.liveicon_width,self.settings.liveicon_height))
            ship.rect.x=10+(ship.rect.width)*ship_num
            ship.rect.y=10
            self.ships.add(ship)         

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_image_rect)
        self.ships.draw(self.screen)          
