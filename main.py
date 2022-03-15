import pygame
from settings import *
from assets import *

class GameState:
    run = True
    clock = pygame.time.Clock()
    active_window = "main"


gameState = GameState()
if "__main__" == __name__:
    
    while gameState.run:
        gameState.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState.run = False
                pygame.quit()
        
        if gameState.active_window == "main":
            pass
        
        pygame.display.update()
