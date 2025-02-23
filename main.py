from baseapp import logging
from baseapp import app_settings
from wsgi import server

if __name__ == "__main__":

    # Activate logging function
    log = logging.Log("MAIN")
    log.write_info("Start logging")
    # Activate settings mechanism
    settings = app_settings.Settings()
    # Trying to start web server
    try:
        server.run()
    except Exception as ServerRunError:
        log.write_error(f"Error caused while service running, {ServerRunError}")
