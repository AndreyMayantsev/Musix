import logging
import os.path
import json

from musix_app.core import base_filesystem, app_config, system_info

log = logging.getLogger("musix.settings")


class Settings:

    __SETTINGS = {}

    def __init__(self, settings_file=".settings"):
        self.log = log
        self.log.info("Starting settings module")
        self.filesystem = base_filesystem.BaseFilesystem()
        self.system_info = system_info.get_system_info()
        self.settings_folder = os.path.join(self.system_info.USER_HOME, app_config.application['HOME_FOLDER'])
        self.filesystem.make_folder_if_not_exists(self.settings_folder)
        self.settings_file = os.path.join(self.settings_folder, settings_file)
        if not os.path.exists(self.settings_file):
            self.filesystem.rewrite_text_file(self.settings_file, '{}')
        self.load_settings()

    def save_settings(self):
        self.log.info(f'Settings {self.__SETTINGS} saved to disk')
        self.filesystem.rewrite_text_file(self.settings_file, json.dumps(self.__SETTINGS))

    def load_settings(self):
        try:
            self.__SETTINGS = json.loads(self.filesystem.read_text_file(self.settings_file))
        except Exception as err:
            self.log.error(f"Can not load settings. Error: {err}")

    def set_setting(self, param, payload):
        self.__SETTINGS[param] = payload

    def get_setting(self, param):
        if param in self.__SETTINGS.keys():
            return self.__SETTINGS[param]
        else:
            self.log.error(f'Settings not contains param: {param}')
            return False

    def del_setting(self, name):
        try:
            del self.__SETTINGS[name]
            self.log.info(f"Setting [{name}] removed")
        except KeyError:
            self.log.error(f"Key [{name}] not founded in settings!")

    def __str__(self):
        return str(self.__SETTINGS)
