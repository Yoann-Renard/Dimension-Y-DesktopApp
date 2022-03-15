from ntpath import join
from pygame import image, display
from os.path import join
#### IMAGES ####
WIN_ICON = image.load(join("assets", "res", "images", "icons", "app-icon.png"))

#### SOUND EFFECTS ####

#### MUSICS ####

#### SETUP ####
display.set_icon(WIN_ICON)

print("Assets init done.")