import os
import requests
import json

from settings import GET_HEROES_FROM_USER_ENDPOINT, HEROES_SERVICE_ENDPOINT, HOST

class Game:
    running_state = True
    clock = None
    active_window = "welcome"
    user_info = {
        "username": ""
    }
    heroes = []

    def __init__(self, clock) -> None:
        self.clock = clock
        self.user_info["username"] = self._getUserName()
        if self.user_info["username"]:
            self._requestUserInfo()
            # TODO PARSE USER INFO
            self._requestHeroes()
            # TODO GET HEROES

    def changeActivity(self, activity: str = "main") -> None:
        self.active_window = activity

    def _getUserName(self) -> str:
        result: str = ""
        try:
            with open(os.path.join("cache", "user_cache.json"),"r") as f:
                json_file = json.load(f)
                result = json_file["username"]
                print("User Name loaded from cache: " + result)
                del json_file, f
        except Exception as e:
            print("Username cannot be loaded from cache.\n"+str(e) )
            # TODO GET USERNAME
        return result

    def _requestUserInfo(self) -> None:
        pass  # TODO
    
    def _requestHeroes(self) -> None:
        result = requests.get(url=HOST+HEROES_SERVICE_ENDPOINT+self.user_info["username"]+GET_HEROES_FROM_USER_ENDPOINT, timeout=5)
        list = json.loads(result.text)["heroes"]
        print("HEROES REQUEST RESPONSE: "+ str(result.status_code) + "\nRESULT LENGTH: "+str(len(list)))
        self.heroes = list

    def _saveHeroesImagesInCache(self) -> None:
        pass

    def _saveUserInfoInCache(self) -> None:
        pass
