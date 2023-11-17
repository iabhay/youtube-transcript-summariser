import logging
from config.log_config.log_config import LogStatements
logger = logging.getLogger('exception_handler')


def handle_exceptions(default_response="Enter Carefully."):
    def decorator(func):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    # Call the original function
                    return func(*args, **kwargs)
                except ValueError:
                    print("Enter Numbers only.")
                except Exception as e:
                    # Handle the exception and provide the default response
                    print(f"Exception occurred: {e}")
                    print(default_response)
        return wrapper
    return decorator


def db_exception(default_success_response="", default_failure_response=LogStatements.log_exception_message):
    def decorator(func):
        def wrapper(*args, **kwargs):
                try:
                    # Call the original function
                    logger.info(default_success_response)
                    return func(*args, **kwargs)
                except ValueError as e:
                    print("Enter Numbers only.")
                    logger.info(e)
                except Exception as e:
                    # Handle the exception and provide the default response
                    # print(f"Exception occurred: {e}")
                    # print(default_failure_response)
                    print("Something Unexpected Occurred. Our team will look into this.")
                    logger.debug(e)
        return wrapper
    return decorator
