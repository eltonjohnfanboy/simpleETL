import logging

def init_logger():
    logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Start of program and logger.')