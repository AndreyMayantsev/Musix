import core.os_propertis_factory as pf

if __name__ == "__main__":
    
    propertis = pf.os_propertis_factory().os_propertis()
    print(f"{propertis.get_os_name()}")