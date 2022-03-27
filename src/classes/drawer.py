# import  pygame
import pygame
from assets import *
from settings import MAIN_FONT, SMOOTH_BLACK, SMOOTH_WHITE, USER_INFO_WIN_HEIGHT, WIN, WIN_WIDTH, WIN_HEIGHT


class Drawer:
    press_any_key_fade = 0
    pygame.font.init()
    USER_WIN_FONT = pygame.font.SysFont(MAIN_FONT, 20)

    def draw_welcome(self, current_ticks) -> None:
        if current_ticks % 1600 < 800:
            self.press_any_key_fade = 255
        else:
            self.press_any_key_fade = 0
        PRESS_ANY_KEY.set_alpha(self.press_any_key_fade)
        WIN.blit(INTRO_BG, (0, 0))
        WIN.blit(INTRO_TEXT,
                    (WIN_WIDTH // 2 - INTRO_TEXT.get_width() // 2, WIN_HEIGHT // 2 - INTRO_TEXT.get_height()))
        WIN.blit(PRESS_ANY_KEY, (WIN_WIDTH // 2 -
                 PRESS_ANY_KEY.get_width() // 2, WIN_HEIGHT // 2 + 50))

    input_text_active = False

    def draw_login(self) -> None:
        WIN.fill((150, 0, 0))

    def draw_main(self, game) -> None:
        WIN.fill((150, 150, 150))
        self.draw_user_info(game)

    def draw_user_info(self, game) -> None:
        # Draw info top window
        pygame.draw.rect(WIN, SMOOTH_BLACK, pygame.rect.Rect(0,0, WIN_WIDTH, USER_INFO_WIN_HEIGHT))
        username = self.USER_WIN_FONT.render("User: "+game.user_data["username"], 1, SMOOTH_WHITE)
        WIN.blit(username, (10, USER_INFO_WIN_HEIGHT*0.1))