import logging

# Create a custom log formatter
class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[94m',  # Blue
        'INFO': '\033[92m',   # Green
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',   # Red
        'CRITICAL': '\033[91m'  # Red
    }
    RESET = '\033[0m'

    def format(self, record):
        log_time = self.formatTime(record).split(' ')[1].split(',')[0]
        log_level = f"[{record.levelname}]"
        log_name = f"[{record.name}]"
        log_message = record.getMessage()
        color = self.COLORS.get(record.levelname, self.RESET)
        return f"[{log_time}]{color}{log_level}{log_name}{self.RESET} {log_message}"



def test():
    # Create a logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # Create a console handler with the custom formatter
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(ColoredFormatter("%(levelname)s: %(message)s"))

    # Add the console handler to the logger
    logger.addHandler(console_handler)

    # Log messages with different log levels
    logger.debug('This is a debug message.')
    logger.info('This is an info message.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
    logger.critical('This is a critical message.')

if __name__ == "__main__":
    test()