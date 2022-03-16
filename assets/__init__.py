from random import choice
from pygame import image, display, transform
from os.path import join

from settings import WIN_HEIGHT, WIN_WIDTH
#### IMAGES ####
WIN_ICON = image.load(join("assets", "res", "images", "icons", "app-icon.png"))
RANDOM_BG = choice(("bg1.png", "bg2.png", "bg3.png",
                    "bg4.png", "bg5.jpg", "bg6.png", "bg7.png"))
INTRO_BG = transform.scale(image.load(join(
    "assets", "res", "images", "backgrounds", RANDOM_BG)), (WIN_WIDTH, WIN_HEIGHT))

#### TEXT IMAGES ####
INTRO_TEXT = image.load(join("assets", "res", "fonts", "title_effect2.png"))
PRESS_ANY_KEY = transform.scale(image.load(join("assets", "res", "fonts", "press_key_w.png")), (200, 20))

#### SOUND EFFECTS ####

#### MUSICS ####

#### SETUP ####
display.set_icon(WIN_ICON)

print("Assets init done.")