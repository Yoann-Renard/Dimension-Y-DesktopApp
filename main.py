import sys
import pygame
from src.classes.event_handler import EventHandler

from src.classes.drawer import Drawer
from settings import *
# from assets import *
from src.classes.game import Game

if "__main__" == __name__:
    game = Game(pygame.time.Clock())
    drawer = Drawer()
    eventHandler = EventHandler()
    while game.running_state:
        game.clock.tick(FPS)
        events = pygame.event.get()

        # GENERAL EVENTS
        for event in events:
            if event.type == pygame.QUIT:
                game.running_state = False
                pygame.quit()
                sys.exit()

        if game.active_window == "main":
            drawer.draw_main(game)
        elif game.active_window == "welcome":
            drawer.draw_welcome(pygame.time.get_ticks())
            eventHandler.welcome_event_handler(events, game, pygame.KEYDOWN)
        elif game.active_window == "login":
            eventHandler.login_event_handler(events, drawer, pygame.MOUSEBUTTONDOWN)
            drawer.draw_login()

        pygame.display.update()
