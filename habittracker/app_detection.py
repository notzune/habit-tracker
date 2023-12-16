import platform


# For Windows
def get_active_window_title_windows():
    import pygetwindow as gw
    try:
        return gw.getActiveWindow().title
    except AttributeError:
        # This handles cases where the active window might not have a title attribute
        return None


# For MacOS
def get_active_window_title_macos():
    from AppKit import NSWorkspace
    active_app = NSWorkspace.sharedWorkspace().frontmostApplication()
    return active_app.localizedName()


# For Linux
def get_active_window_title_linux():
    from Xlib import display
    d = display.Display().screen()
    window = d.root.query_tree().children[-1]
    return window.get_wm_name()


def get_active_window_title():
    os_name = platform.system()
    if os_name == 'Windows':
        return get_active_window_title_windows()
    elif os_name == 'Darwin':
        return get_active_window_title_macos()
    elif os_name == 'Linux':
        return get_active_window_title_linux()
    else:
        raise NotImplementedError("OS not supported")


# Example usage
if __name__ == "__main__":
    print(f"The active window is: {get_active_window_title()}")
