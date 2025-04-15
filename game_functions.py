import pygame
import sys
from bullet import Bullet
from alien import Alien
import time
#respoding to keyboard and mouse presses

def check_events(ship,screen,bg_settings,bullets,Play_button,stats,Aliens,sb,bullet_sound):
 event_list=pygame.event.get()

 for event in event_list:
    
    if event.type==pygame.QUIT:
       sys.exit()
       
    elif event.type==pygame.MOUSEBUTTONDOWN:
        check_play_button(Play_button,stats,bullets,Aliens,screen,bg_settings,ship,sb)

    elif event.type==pygame.KEYDOWN:
       check_keydown_events(event,ship,screen,bg_settings,bullets,stats,Aliens,sb,bullet_sound)

    elif event.type==pygame.KEYUP:
      check_Keyup_events(event,ship)

def check_Keyup_events(event,ship):

   if event.key==pygame.K_RIGHT:
          ship.moving_right=False

   elif event.key==pygame.K_LEFT:
          ship.moving_left=False

def check_keydown_events(event,ship,screen,bg_settings,bullets,stats,Aliens,sb,bullet_sound):
        
        if event.key==pygame.K_RIGHT:
          ship.moving_right=True

        elif event.key==pygame.K_LEFT:
             ship.moving_left=True

        elif event.key== pygame.K_SPACE:
           fire_bullet(bullets,bg_settings,screen,ship,bullet_sound)

        elif event.key==pygame.K_q:
            sys.exit()  

        elif event.key==pygame.K_p:
             game_start(stats,bullets,Aliens,bg_settings,ship,screen,sb)
                

def update_screen(screen,bg_settings,ship,bullets,Aliens,Play_button,stats,sb,bg_image):
  draw_background(screen,bg_image)
  ship.blitme()   
  bullets.draw(screen)
  Aliens.draw(screen)
  sb.show_score()
  if not stats.game_active:
    Play_button.draw()
  pygame.display.flip()
       
def update_bullet(bullets,Aliens,screen,bg_settings,stats,sb,alien_hit_sound):
   for bullet in bullets:
        bullet.update()
        if bullet.rect.bottom<=0: #delete the bullets once they are off screen
             bullets.remove(bullet)
   detect_collisions(bullets,Aliens,bg_settings,screen,stats,sb,alien_hit_sound)     
   
def detect_collisions(bullets,Aliens,bg_settings,screen,stats,sb,alien_hit_sound):
      
      collisions=pygame.sprite.groupcollide(bullets,Aliens,True,True)    
      if collisions:
         alien_hit_sound.play()
         for aliens in collisions.values():
           stats.score+=bg_settings.alien_points*len(aliens)
         sb.prep_score()
         check_high_score(stats,sb)  
        

      if len(Aliens)==0:
       bg_settings.increase_speed()
       stats.level+=1
       sb.prep_level()
       bullets.empty()
       Aliens.empty()
       create_fleet(screen,bg_settings,Aliens)

def fire_bullet(bullets,bg_settings,screen,ship,bullet_sound):
     
     #limiting the number of bullets that 
     #can be fired on screen at once

     if len(bullets)<bg_settings.allowed_bullet:
             new_bullet=Bullet(screen,ship,bg_settings)
             bullets.add(new_bullet)
             bullet_sound.play()
def number_rows(bg_settings,alien_height):
    available_space_y=bg_settings.screen_height-(alien_height+bg_settings.start_y)
    num_rows=int(available_space_y/(alien_height+bg_settings.space_y) )
    return num_rows

def number_aliens(bg_settings,alien_width):
     available_space_x=bg_settings.screen_width-(alien_width+bg_settings.start_x)
     num_aliens=int(available_space_x/(alien_width+bg_settings.space_x))
     return num_aliens

def create_aliens(bg_settings,screen,Aliens,alien_width,alien_height,row_num,num_aliens):
    for alien_num in range(num_aliens-6):
       new_alien=Alien(screen,bg_settings)
       new_alien.x=bg_settings.start_x+alien_num*(alien_width+bg_settings.space_x)
       new_alien.rect.x=new_alien.x
       new_alien.y=bg_settings.start_y+row_num*(alien_height+bg_settings.space_y)
       new_alien.rect.y=new_alien.y
       Aliens.add(new_alien)

def create_fleet(screen,bg_settings,Aliens):
     alien=Alien(screen,bg_settings)
     alien_height=alien.rect.height
     alien_width=alien.rect.width

     num_rows=number_rows(bg_settings,alien_height)
     num_aliens= number_aliens(bg_settings,alien_width)

     for row_num in range(num_rows-5):
          create_aliens(bg_settings,screen,Aliens,alien_width,alien_height,row_num,num_aliens)
     
def update_aliens(Aliens,bg_settings,ship,stats,bullets,screen,sb):
      Aliens.update()
      check_fleet_edges(Aliens,bg_settings)
      check_ship_alien_collision(ship,Aliens,stats,bullets,screen,bg_settings,sb)
      check_aliens_bottom(Aliens,ship,stats,bullets,screen,bg_settings,sb)

def check_fleet_edges(Aliens,bg_settings):
    for alien in Aliens.sprites():
       if alien.check_edges():
         change_fleet_direction(bg_settings,Aliens)
         break
       
def change_fleet_direction(bg_settings,Aliens) :
      for alien in Aliens.sprites():
           alien.y+=bg_settings.fleet_drop_speed
           alien.rect.y=alien.y
      bg_settings.fleet_direction*=-1      

def ship_hit(ship,Aliens,stats,bullets,screen,bg_settings,sb):
  
     if stats.ship_left>1:   
          
         stats.ship_left-=1
         sb.prep_ships()
         bullets.empty()
         Aliens.empty()
         ship.center_ship()
         create_fleet(screen,bg_settings,Aliens)
         pygame.time.delay(500) # delay the game by half second

     else:
         stats.game_active=False
         pygame.mouse.set_visible(True)


def check_ship_alien_collision(ship,Aliens,stats,bullets,screen,bg_settings,sb):
     if pygame.sprite.spritecollideany(ship,Aliens):
         ship_hit(ship,Aliens,stats,bullets,screen,bg_settings,sb)

def check_aliens_bottom(Aliens,ship,stats,bullets,screen,bg_settings,sb):
    for alien in Aliens.sprites():
        if alien.rect.bottom>=alien.screen_rect.bottom:
              ship_hit(ship,Aliens,stats,bullets,screen,bg_settings,sb)
              break

def update_sprites(stats,ship,bullets,Aliens,screen,bg_settings,sb,alien_hit_sound):
     if stats.game_active :
          ship.update()
          update_bullet(bullets,Aliens,screen,bg_settings,stats,sb,alien_hit_sound)
          update_aliens(Aliens,bg_settings,ship,stats,bullets,screen,sb)   

def check_play_button(Play_button,stats,bullets,Aliens,screen,bg_settings,ship,sb):
    mouse_x,mouse_y=pygame.mouse.get_pos()
    if not stats.game_active and Play_button.rect.collidepoint(mouse_x,mouse_y):
             game_start(stats,bullets,Aliens,bg_settings,ship,screen,sb)

def game_start(stats,bullets,Aliens,bg_settings,ship,screen,sb):
              pygame.mouse.set_visible(False)

              bg_settings.initialize_dynamic_settings()

              stats.reset_stats()
              sb.prep_ships()
              stats.game_active=True

              bullets.empty()
              Aliens.empty()
              
              sb.prep_score()
              sb.prep_high_score()
              sb.prep_level()

              create_fleet(screen,bg_settings,Aliens)
              ship.center_ship()

def check_high_score(stats,sb):
    if stats.high_score<stats.score:
             stats.high_score=stats.score
             sb.prep_high_score()

def draw_background(screen,bg_image):
   screen.blit(bg_image,(0,0))