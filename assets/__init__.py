from pygame import image, display
from os.path import join
#### IMAGES ####
WIN_ICON = image.load(join("assets", "res", "images", "icons", "app-icon.png"))
INTRO_BG = image.load(join("assets","res","images", "backgrounds", "intro_bg.gif"))

#### SOUND EFFECTS ####

#### MUSICS ####

#### SETUP ####
display.set_icon(WIN_ICON)

print("Assets init done.")