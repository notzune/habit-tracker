import time

# Dictionary to keep track of time spent on each application
time_spent = {}

# Variable to remember the last checked application and its start time
last_app_name = None
last_start_time = None


def start_timer(app_name):
    global last_app_name, last_start_time
    # If there's an app already being tracked, stop the timer for it first
    if last_app_name is not None:
        stop_timer()
    # Start the timer for the new app
    last_app_name = app_name
    last_start_time = time.time()


def stop_timer():
    global last_app_name, last_start_time
    if last_app_name is not None:
        # Calculate the time spent on the last app
        elapsed_time = time.time() - last_start_time
        # Update the time spent dictionary
        time_spent[last_app_name] = time_spent.get(last_app_name, 0) + elapsed_time
        # Reset the last app name and start time
        last_app_name = None
        last_start_time = None


def get_time_spent():
    # Return the time spent dictionary
    return time_spent


# Example usage
if __name__ == "__main__":
    start_timer("ExampleApp")
    time.sleep(5)  # Simulate the app being in use for 5 seconds
    stop_timer()
    print(get_time_spent())
