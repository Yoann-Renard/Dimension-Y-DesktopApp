
import pygame
from settings import *
from assets import *
from src.classes.game import Game


game = Game(clock=pygame.time.Clock())
if "__main__" == __name__:
    while game.run_state:
        game.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.run_state = False
                pygame.quit()
        
        if game.active_window == "main":
            pass
        
        pygame.display.update()
