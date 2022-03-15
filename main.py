import json
import os
import pygame
from settings import *
from assets import *


    
class Game:
    run_state = True
    clock = pygame.time.Clock()
    active_window = "main"
    user_info = {
        "user_name": ""
    }
    
    def __init__(self) -> None:
        self.user_info["user_name"] = self._getUserName()
        self._requestUserInfo()
        
        # TODO GET HEROES
    
    def changeActivity(self, activity: str = "main") -> None:
        self.active_window = activity

    def _getUserName(self) -> str:
        result: str = ""
        try:
            with open(os.path.join("cache", "user_cache.json")) as f:
                json = json.load(f)
                result = json["user_name"]
                del json, f
        except:
            print("User Name cannot be loaded from cache.")
            # TODO GET USERNAME
        return result
    
    def _requestUserInfo(self) -> None:
        pass # TODO
        
    


game = Game()
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
