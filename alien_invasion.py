import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
pygame.mixer.init()

def run_game():

    pygame.init()  
    bg_settings=Settings()   
    screen=pygame.display.set_mode((bg_settings.screen_width,bg_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship=Ship(screen,bg_settings)
    bullets=Group()
    Aliens=Group()

    stats=GameStats(bg_settings)
    Play_button=Button(screen,bg_settings,"Play")
    gf.create_fleet(screen,bg_settings,Aliens)
    sb=Scoreboard(screen,bg_settings,stats)

    bg_image=pygame.image.load("images/background.bmp").convert()
    bg_image=pygame.transform.scale(bg_image,(bg_settings.screen_width,bg_settings.screen_height))

    bullet_sound=pygame.mixer.Sound('sounds/audio_ship_cannon.wav')
    alien_hit_sound=pygame.mixer.Sound('sounds/audio_alien_hit.wav')

    while True:
        gf.check_events(ship,screen,bg_settings,bullets,Play_button,stats,Aliens,sb,bullet_sound)
        gf.update_sprites(stats,ship,bullets,Aliens,screen,bg_settings,sb,alien_hit_sound)
        gf.update_screen(screen,bg_settings,ship,bullets,Aliens,Play_button,stats,sb,bg_image)
      
        
run_game()  
