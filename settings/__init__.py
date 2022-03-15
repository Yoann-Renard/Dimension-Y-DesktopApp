from pygame import display

#
##
###
#### WINDOW #### WINDOW ####
WIN_WIDTH = 1200
WIN_HEIGHT = 800

CAPTION = "Dimension Y"

#
##
###
#### RUNNING #### RUNNING ####
FPS = 60

#
##
###
#### SETUP #### SETUP ####
WIN = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption(CAPTION)
print("settings init done.")