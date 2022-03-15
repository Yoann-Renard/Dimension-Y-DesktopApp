#import  pygame
from assets import *
class Drawer:
    
    def draw_welcome(self, window):
        window.blit(INTRO_BG, (0,0))