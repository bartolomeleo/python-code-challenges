import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Create a logger
logger = logging.getLogger('example_logger')

# Set the logging level
logger.setLevel(logging.DEBUG)

# Create a StreamHandler
console_handler = logging.StreamHandler()

# Set the logging level of the handler
console_handler.setLevel(logging.DEBUG)

# Create a Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add the Formatter to the handler
console_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(console_handler)

# Log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
