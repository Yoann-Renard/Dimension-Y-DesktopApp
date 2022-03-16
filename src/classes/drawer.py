#import  pygame
from assets import *
from settings import WIN_WIDTH, WIN_HEIGHT
class Drawer:
    press_any_key_fade = 0
    def draw_welcome(self, window, current_ticks) -> None:
        if current_ticks % 1600 < 800:
            self.press_any_key_fade = 255
        else:
            self.press_any_key_fade = 0
        PRESS_ANY_KEY.set_alpha(self.press_any_key_fade)
        window.blit(INTRO_BG, (0,0))
        window.blit(INTRO_TEXT, ( WIN_WIDTH//2 - INTRO_TEXT.get_width()//2, WIN_HEIGHT//2 - INTRO_TEXT.get_height()))
        window.blit(PRESS_ANY_KEY, ( WIN_WIDTH//2 - PRESS_ANY_KEY.get_width()//2, WIN_HEIGHT//2 + 50))
    
    input_text_active = False
    def draw_login(self) -> None:
        pass
    
    def draw_main(self) -> None:
        pass