import os
import datetime
from . import system_info
from . import app_config
from . import base_filesystem


class Log:

    LOG_FOLDER_NAME = "LOGS"
    LOG_FOLDER_SEPARATE_BY_DATE = True
    WRITE_IN_HOME_FOLDER = True
    LOG_NAME = "log"
    DATE_NOW = datetime.datetime.today().strftime('%Y-%m-%d')
    DEFAULT_FILENAME = "log.log"

    def __init__(self, name):
        self.filesystem = base_filesystem.BaseFilesystem()
        self.system_folders = system_info.get_system_info()
        self.application_data = os.path.join(self.system_folders.USER_HOME, app_config.application['HOME_FOLDER'])
        self.LOG_NAME = name
        self.dir = self.application_data if self.WRITE_IN_HOME_FOLDER else os.path.abspath(os.curdir)
        self.log_dir = os.path.join(self.dir, self.LOG_FOLDER_NAME)
        if self.filesystem.folder_exists(self.application_data):
            if self.filesystem.folder_exists(self.log_dir):
                if self.LOG_FOLDER_SEPARATE_BY_DATE:
                    self.filesystem.folder_exists(os.path.join(self.log_dir, self.DATE_NOW))
                    self.log_dir = self.log_dir + self.DATE_NOW

        self.DEFAULT_FILENAME = "/" + self.LOG_NAME + "-" + self.DATE_NOW + ".log"
        self.__write_log('=========== START LOGGING ===========')
        self.__write_log(f'Application: {app_config.application["APP_NAME"]}, '
                       f'version: {app_config.application["VERSION"]}')
        self.__write_log(f'\n{str(self.system_folders)}\n')

    def write_info(self, info):
        self.__write_log(f"INFO\t{info}")

    def write_warning(self, warinig):
        self.__write_log(f"WARN\t{warinig}")

    def write_error(self, error):
        self.__write_log(f"ERROR\t{error}")

    def __write_log(self, logtext):
        time = datetime.datetime.today().strftime('%X')
        if self.LOG_FOLDER_SEPARATE_BY_DATE:
            self.__actualize_log_folder()
        self.filesystem.append_text_file(self.log_dir + self.DEFAULT_FILENAME, time + ": " + logtext + "\n")

    def __actualize_log_folder(self):
        self.DATE_NOW = datetime.datetime.today().strftime('%Y-%m-%d')
        self.log_dir = os.path.join(self.dir, self.LOG_FOLDER_NAME, self.DATE_NOW)
        self.filesystem.folder_exists(self.log_dir)