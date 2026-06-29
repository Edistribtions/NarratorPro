from narratorpro.config.config_manager import ConfigManager
from narratorpro.logging.logger import get_logger

def main():
    cfg=ConfigManager()
    log=get_logger()
    log.info("NarratorPro started")
    print("NarratorPro v0.1.0-alpha1")

if __name__=="__main__":
    main()
