import logging

# Create a logger
logger = logging.getLogger('Database')
logger.setLevel(logging.INFO)

# Create a file handler
handler = logging.FileHandler('Database_log.log')
handler.setLevel(logging.INFO)

# Create a logging format
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)