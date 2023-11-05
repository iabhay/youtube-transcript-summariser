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
