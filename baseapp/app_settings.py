import os.path
import json

from . import base_filesystem
from . import logging
from . import system_info
from . import app_config


class Settings:

    __SETTINGS = {}

    def __init__(self):
        self.log = logging.Log("Settings")
        self.log.write_info("Starting settings module")
        self.filesystem = base_filesystem.BaseFilesystem()
        self.system_info = system_info.get_system_info()
        self.settings_folder = os.path.join(self.system_info.USER_HOME, app_config.application['HOME_FOLDER'])
        self.filesystem.make_folder_if_not_exists(self.settings_folder)
        self.settings_file = os.path.join(self.settings_folder, '.settings')
        if not os.path.exists(self.settings_file):
            self.filesystem.rewrite_text_file(self.settings_file, '{}')
        self.load_settings()

    def save_settings(self):
        self.log.write_info(f'Settings {self.__SETTINGS} saved to disk')
        self.filesystem.rewrite_text_file(self.settings_file, json.dumps(self.__SETTINGS))

    def load_settings(self):
        try:
            self.__SETTINGS = json.loads(self.filesystem.read_text_file(self.settings_file))
        except Exception as err:
            self.log.write_error(f"Can not load settings. Error: {err}")

    def set_setting(self, param, payload):
        self.__SETTINGS[param] = payload

    def get_setting(self, param):
        if param in self.__SETTINGS.keys():
            return self.__SETTINGS[param]
        else:
            self.log.write_error(f'Settings not contains param: {param}')
            return False

    def del_setting(self, name):
        try:
            del self.__SETTINGS[name]
            self.log.write_info(f"Setting [{name}] removed")
        except KeyError:
            self.log.write_error(f"Key [{name}] not founded in settings!")
