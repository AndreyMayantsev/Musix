import os
from . import os_propertis


class os_propertis_windows(os_propertis):

    def __init__(self):
        # Call base initiation
        super.__init__()

        print("Windows propertis getter started!")

        self.propertis = { }
        self.settings["os_type"] =     os.name
        self.settings["os_name"] =     os.environ['OS']
        self.settings["os_username"] = os.environ['USERNAME']
        self.settings["os_userhome"] = os.path.join(os.environ["HOMEDRIVE"], os.environ['HOMEPATH'])

        print(f"Windows propertis: {self.propertis}")
    
    # system propertis getters
    def os_get_name(self):
        return self.propertis["os_name"]
    
    def os_get_username(self):
        return self.propertis["os_username"]
    
    def os_get_userhome(self):
        return self.propertis["os_userhome"]