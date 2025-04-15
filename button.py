import pygame.font

class Button:
    def __init__(self,screen,bg_settings,msg):
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.settings=bg_settings

        self.width,self.height=200,50
        self.colour=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)

        self.rect=pygame.Rect((0,0,self.width,self.height))
        self.rect.center=self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self,msg):
        self.msg_image=self.font.render(msg,True,self.text_color,self.colour) 
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center   

    def draw(self):
        self.screen.fill(self.colour,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)



