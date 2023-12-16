from datetime import time

from habittracker import app_detection, time_tracking, config_manager, calendar_sync


def main():
    # Load configuration
    config = config_manager.load_config()

    while True:
        # Get the current active application
        active_app = app_detection.get_active_application()

        # Check if it's in the list of apps to track
        if active_app in config['tracked_apps']:
            time_tracking.start_timer(active_app)
        else:
            time_tracking.stop_timer()

        # Periodically sync with Google Calendar
        calendar_sync.check_and_update()

        # Sleep for a bit to avoid hogging CPU
        time.sleep(1)


if __name__ == "__main__":
    main()
