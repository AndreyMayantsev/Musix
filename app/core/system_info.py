import os


def get_system_info():
    os_type = os.name
    if os_type == 'nt':
        return SystemInfoWindows()
    else:
        os_name = os.uname()[0]
        if os_name == 'Linux':
            return SystemInfoLinux()
        if os_name == 'Darwin':
            return SystemInfoDarwin()
        else:
            raise EnvironmentError("Unknown OS type!")


class SystemInfoWindows:

    def __init__(self):
        # Folders
        self.SYSTEM_DRIVE = os.environ['SYSTEMDRIVE']
        self.USER_HOME = os.path.join(self.SYSTEM_DRIVE, os.environ['HOMEPATH'])
        self.PROGRAMS_DATA = os.environ['PROGRAMDATA']
        self.TEMPORARY_FILES = os.environ['TEMP']
        # Info
        self.HOST_NAME = os.environ['COMPUTERNAME']
        self.OS_NAME = os.environ['OS']
        self.USER_NAME = os.environ['USERNAME']
        # Hardware
        self.PROCESSOR_INFO = {
            "NAME": os.environ['PROCESSOR_IDENTIFIER'],
            "ARCH": os.environ['PROCESSOR_ARCHITECTURE'],
            "CORES": os.environ['NUMBER_OF_PROCESSORS']
        }

    def __str__(self):
        return f"About system:\nOS: {self.OS_NAME} on host {self.HOST_NAME}, active user: {self.USER_NAME}\n" \
               f"Home folder: {self.USER_HOME}\nHW_PROC: {self.PROCESSOR_INFO}"


class SystemInfoLinux:

    def __init__(self):
        # Folders
        self.USER_HOME = os.environ['HOME']
        self.PROGRAMS_DATA = '/opt'
        self.TEMPORARY_FILES = '/tmp'
        # Info
        self.HOST_NAME = os.uname()[1]
        self.OS_NAME = os.uname()
        self.USER_NAME = os.environ['USER']
        # Hardware
        self.PROCESSOR_INFO = {
            "ARCH": os.uname()[4],
        }

    def __str__(self):
        return f"About system:\nOS: {self.OS_NAME} on host {self.HOST_NAME}, active user: {self.USER_NAME}\n" \
               f"Home folder: {self.USER_HOME}\nHW_PROC: {self.PROCESSOR_INFO}"


class SystemInfoDarwin:

    def __init__(self):
        # Folders
        self.USER_HOME = os.environ['HOME']
        self.PROGRAMS_DATA = '/opt'
        self.TEMPORARY_FILES = '/tmp'
        # Info
        self.HOST_NAME = os.uname()[1]
        self.OS_NAME = os.uname()
        self.USER_NAME = os.environ['USER']
        # Hardware
        self.PROCESSOR_INFO = {
            "ARCH": os.uname()[4],
        }

    def __str__(self):
        return f"About system:\nOS: {self.OS_NAME} on host {self.HOST_NAME}, active user: {self.USER_NAME}\n" \
               f"Home folder: {self.USER_HOME}\nHW_PROC: {self.PROCESSOR_INFO}"

