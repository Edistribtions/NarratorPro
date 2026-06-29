from pathlib import Path
import json


class ConfigurationService:

    def __init__(self):

        self.settings_dir = (
            Path.home()
            / ".narratorpro"
        )

        self.settings_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.settings_file = (
            self.settings_dir
            / "settings.json"
        )

        self.settings = {}

        self.load()

    def load(self):

        if self.settings_file.exists():

            self.settings = json.loads(
                self.settings_file.read_text(
                    encoding="utf-8"
                )
            )

    def save(self):

        self.settings_file.write_text(
            json.dumps(
                self.settings,
                indent=4
            ),
            encoding="utf-8",
        )

    def get(self, key, default=None):

        return self.settings.get(key, default)

    def set(self, key, value):

        self.settings[key] = value