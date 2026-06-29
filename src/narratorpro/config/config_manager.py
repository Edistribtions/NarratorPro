from pathlib import Path
import json

class ConfigManager:
    def __init__(self):
        self.path=Path("config/config.json")
        self.path.parent.mkdir(exist_ok=True)
        if not self.path.exists():
            self.path.write_text(json.dumps({
                "output_dir":"output",
                "log_level":"INFO"
            },indent=2))
        self.data=json.loads(self.path.read_text())
