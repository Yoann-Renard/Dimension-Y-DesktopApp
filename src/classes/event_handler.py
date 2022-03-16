class EventHandler:
    
    def welcome_event_handler(self, events, game, key):
        for event in events:
            if event.type == key:
                if game.user_info["username"]:
                    game.changeActivity("main")
                else:
                    game.changeActivity("login")
    
    def login_event_handler(self, events, drawer, key):
        for event in events:
            if event.type == key:
                if True:  # input_rect.collidepoint(event.pos)
                    drawer.input_text_active = True
                else:
                    drawer.input_text_active = False
