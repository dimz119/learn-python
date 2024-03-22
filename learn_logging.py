import logging

# root logger
# Configure logging to print to console with a specific format and level
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# # Now, you can log messages at different severity levels
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# # Write the log to the file
# logging.basicConfig(
#     filename='example.log',
#     level=logging.DEBUG,
#     format='%(asctime)s - %(levelname)s - %(message)s')

# # Now, we can log to the root logger at different severity levels
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


# # custom logger
# logger = logging.getLogger('my_logger')
# logger.setLevel(logging.DEBUG)  # Set the log level to DEBUG to capture all types of log messages

# # Create a console handler and set the level to debug
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)

# # Optionally, create a formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# # Set the formatter for the console handler
# console_handler.setFormatter(formatter)

# # Add the console handler to the logger
# logger.addHandler(console_handler)

# # Create a file handler, write logs to 'my_app.log'
# file_handler = logging.FileHandler('my_app.log')
# file_handler.setLevel(logging.DEBUG)

# # Set the formatter for the file handler
# file_handler.setFormatter(formatter)

# # Add the file handler to the logger
# logger.addHandler(file_handler)

# # Example logging messages
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')
