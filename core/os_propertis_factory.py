import os
from . import os_propertis_windows


class os_propertis_factory:

    def os_propertis(cls):
        if os.name == 'nt':
            return os_propertis_windows()
        else:
            os_name = os.uname()[0]
            if os_name == 'Linux':
                return 'linux'
            if os_name == 'Darwin':
                return 'macOS'
            else:
                print("Can not determinate Operation System type! This program must be run in linux/windows/macOS.")
                raise Exception("Can not determinate Operation System type!")