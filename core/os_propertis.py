import os


class engine_os_propertis:

    def __init__(self) -> None:
        print("Engine start...")

        """ 
        Base OS settings: 
        os_type:     nt / posix
        os_name:     Name of OS
        os_username: Name of this user
        os_userhome: Home folder of this user
        """
        self.settings = {
            "os_type": os.name
        }

        print("Getting base information about OS...")
        self.__recognize_os()
        print(f"\n=== SETTINGS ===\n{self.settings}\n")
 

    def __recognize_os(self):
        if self.settings["os_type"] == 'nt':
            self.__win32_settings()
            return 'windows'
        else:
            os_name = os.uname()[0]
            if os_name == 'Linux':
                return 'linux'
            if os_name == 'Darwin':
                return 'macOS'
            else:
                print("Can not determinate Operation System type! This program must be run in linux/windows/macOS.")
                raise Exception("Can not determinate Operation System type!")

    
    def __win32_settings(self):
        self.settings["os_type"] =     os.name
        self.settings["os_name"] =     os.environ['OS']
        self.settings["os_username"] = os.environ['USERNAME']
        self.settings["os_userhome"] = os.path.join(os.environ["HOMEDRIVE"], os.environ['HOMEPATH'])


        