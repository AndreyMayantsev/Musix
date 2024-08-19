from baseapp import logging


if __name__ == "__main__":
    log = logging.Log("MAIN")
    log.write_error("Unknown error :0")
    log.write_info("Stepping next...")
