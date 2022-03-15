import os

class Game:
    run_state = True
    clock = None
    active_window = "main"
    user_info = {
        "user_name": ""
    }

    def __init__(self, clock) -> None:
        self.clock = clock
        self.user_info["user_name"] = self._getUserName()
        self._requestUserInfo()

        # TODO GET HEROES

    def changeActivity(self, activity: str = "main") -> None:
        self.active_window = activity

    def _getUserName(self) -> str:
        result: str = ""
        try:
            with open(os.path.join("cache", "user_cache.json")) as f:
                json = json.load(f)
                result = json["user_name"]
                del json, f
        except:
            print("User Name cannot be loaded from cache.")
            # TODO GET USERNAME
        return result

    def _requestUserInfo(self) -> None:
        pass  # TODO
