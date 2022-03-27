from pygame import display

#
##
###
#### WINDOW #### WINDOW ####
WIN_WIDTH = 1300
WIN_HEIGHT = 800

CAPTION = "Dimension Y"

#
##
###
#### INGAME WINDOWS #### INGAME WINDOWS ####
USER_INFO_WIN_HEIGHT = 100

#
##
###
#### RUNNING #### RUNNING ####
FPS = 60

#
##
###
#### REQUEST #### REQUEST ####
HOST = "http://192.168.0.16"
HEROES_SERVICE_ENDPOINT = ":9990/"
GET_HEROES_FROM_USER_ENDPOINT = "/get_heroes"

#
##
###
#### COLORS #### COLORS ####
SMOOTH_BLACK = (30, 30, 30)
SMOOTH_WHITE = (200, 200, 200)

#
##
###
#### FONTS #### FONTS ####
MAIN_FONT = "arial"

#
##
###
#### SETUP #### SETUP ####
WIN = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption(CAPTION)
print("settings init done.")