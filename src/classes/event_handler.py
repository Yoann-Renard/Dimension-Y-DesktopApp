class EventHandler:
    
    def welcome_event_handler(self, events, game, key):
        for event in events:
            if event.type == key:
                if game.user_data["username"]:
                    game.change_activity("main")
                else:
                    game.change_activity("login")

    def login_event_handler(self, events, drawer, key):
        for event in events:
            if event.type == key:
                if True:  # input_rect.collidepoint(event.pos)
                    drawer.input_text_active = True
                else:
                    drawer.input_text_active = False
