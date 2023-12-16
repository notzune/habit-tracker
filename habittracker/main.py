import time
from datetime import datetime
from app_detection import get_active_window_title
from time_tracking import start_timer, stop_timer, get_time_spent
from config_manager import load_config, get_config_option
from calendar_sync import get_calendar_service, create_or_update_event


def is_new_day(last_check_time):
    return last_check_time.date() != datetime.now().date()


def main():
    config = load_config()
    tracked_apps = get_config_option('tracked_apps')
    update_interval = get_config_option('update_interval')

    last_active_app = None
    last_check_time = datetime.now()

    while True:
        current_app = get_active_window_title()
        if current_app in tracked_apps:
            if current_app != last_active_app:
                stop_timer()  # Stop timer for the previous app
                start_timer(current_app)  # Start timer for the new app
                last_active_app = current_app
        else:
            stop_timer()  # Stop timer if the current app is not being tracked
            last_active_app = None

        # Check if it's a new day
        if is_new_day(last_check_time):
            service = get_calendar_service()
            create_or_update_event(service, get_time_spent())
            last_check_time = datetime.now()  # Reset the last check time

        time.sleep(update_interval)


if __name__ == "__main__":
    main()
