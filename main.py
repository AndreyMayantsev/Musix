from baseapp import logging
from baseapp import app_settings


if __name__ == "__main__":
    log = logging.Log("MAIN")
    log.write_info("Logging started...")
    settings = app_settings.Settings()

    settings.set_setting('UserName', 'plafon')
    settings.set_setting('Passwd', '123ASDQWE123')
    settings.save_settings()
