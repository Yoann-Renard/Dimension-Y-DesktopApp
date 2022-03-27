import io
import os
from itsdangerous import base64_decode
import requests
import json
import base64
from PIL import Image

from settings import GET_HEROES_FROM_USER_ENDPOINT, HEROES_SERVICE_ENDPOINT, HOST


class Game:
    running_state = True
    clock = None
    active_window = "welcome"
    user_data = {
        "username": ""
    }
    heroes = []

    def __init__(self, clock) -> None:
        self.clock = clock
        self.user_data["username"] = self._get_user_name_from_cache()
        if self.user_data["username"]:
            self._request_user_info()
            # TODO PARSE USER INFO
            self._request_heroes()
            self._save_heroes_images_in_cache()

    def change_activity(self, activity: str = "main") -> None:
        self.active_window = activity

    def _get_user_name_from_cache(self) -> str:
        result: str = ""
        try:
            with open(os.path.join("cache", "user_data.json"), "r") as f:
                json_file = json.load(f)
                result = json_file["username"]
                print("User Name loaded from cache: " + result)
                del json_file, f
        except Exception as e:
            print("Username cannot be loaded from cache.\n" + str(e))
            # TODO GET USERNAME
        return result

    def _request_user_info(self) -> None:
        pass  # TODO

    def _request_heroes(self) -> None:
        result = requests.get(
            url=HOST + HEROES_SERVICE_ENDPOINT + self.user_data["username"] + GET_HEROES_FROM_USER_ENDPOINT, timeout=5)
        rlist = json.loads(result.text)["heroes"]
        print("HEROES REQUEST RESPONSE: " + str(result.status_code) + "\nRESULT LENGTH: " + str(len(rlist)))
        self.heroes = rlist

    def _save_heroes_images_in_cache(self) -> None:
        try:
                os.makedirs(os.path.join("cache", "sprites"))
        except OSError:
            pass
        
        count = 0
        for hero in self.heroes:
            
            path = os.path.join("cache", "sprites", f"{hero['_id']}.png")
            if not os.path.exists(path):
                img_byte = io.BytesIO(base64.b64decode(hero["sprite_base64"].split(',')[1]))
                img = Image.open(img_byte)
                img.save(path)
                count += 1
        print(str(count)+' new sprites have been stored in cache.')

    def _save_user_info_in_cache(self) -> None: # FIXME
        with open(os.path.join("cache", "user_data.json"), 'w') as f:
            f.write(json.dumps(self.user_data))
