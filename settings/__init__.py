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
#### RUNNING #### RUNNING ####
FPS = 60

#
##
###
#### REQUEST #### REQUEST
HOST = "http://192.168.0.16"
HEROES_SERVICE_PORT = ":9990/"
GET_HEROES_FROM_USER_ENDPOINT = "/get_heroes"


#
##
###
#### SETUP #### SETUP ####
WIN = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption(CAPTION)
print("settings init done.")