class Settings:
    def __init__(self):
        # background settings
        self.screen_width=1000
        self.screen_height=800
        self.bg_color=(230,230,230)
        self.allowed_ships=3    

        self.ship_width=60
        self.ship_height=48

        self.liveicon_height=32
        self.liveicon_width=40

        self.alien_height=40
        self.alien_width=40
    
        #Bullet Settings
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(255,0,0)
        self.allowed_bullet=3
        
        #Alien settings
        self.fleet_drop_speed=20
        self.fleet_direction=1

        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()
        
        #initial position of the alien
        self.start_x,self.start_y=(50,100) # x and y coordinate of the first alien rect
        self.space_x,self.space_y=(15,15) #spacing between two aliens horizontally and vertically

    def initialize_dynamic_settings(self):
         # settings whose values are not fixed throughout the game
         self.ship_speed_factor=1.2
         self.bullet_speed_factor=1
         self.fleet_moving_factor=0.7 #moving right or left
         self.alien_points=50

    def increase_speed(self): 
        #settings need to be upadated after every level

        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.fleet_moving_factor*=self.speedup_scale     
        self.alien_points*=self.score_scale
       