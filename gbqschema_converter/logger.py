import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d [%(levelname)-5s] [%(name)-12s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def get_logger():
  return logging.getLogger("gbqschema_converter")
