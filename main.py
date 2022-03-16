
import pygame

from src.classes.drawer import Drawer
from settings import *
#from assets import *
from src.classes.game import Game



if "__main__" == __name__:
    game = Game(clock=pygame.time.Clock())
    drawer = Drawer()
    while game.running_state:
        game.clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                game.running_state = False
                pygame.quit()
        
        if game.active_window == "main":
            pass
        elif game.active_window == "welcome":
            drawer.draw_welcome(WIN, pygame.time.get_ticks())
            for event in events:
                if event.type == pygame.KEYDOWN:
                    pass
        
        pygame.display.update()
