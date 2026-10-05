import json
import os


class DataManager:

    def __init__(self):

        self.configs = {
            "music": True,
            "sound": True,
            "volume": 50,
        }

        self.folder = "data"
        self.file = os.path.join(
            self.folder,
            "configs.json"
        )

        os.makedirs(
            self.folder,
            exist_ok=True
        )

        self.load()

    def load(self):

        if not os.path.exists(self.file):
            self.save()
            return

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as file:

            self.configs = json.load(file)

    def save(self):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.configs,
                file,
                indent=4
            )

    def get_data(self, key):

        return self.configs.get(key)

    def change_data(self, key, value):

        self.configs[key] = value
        self.save()