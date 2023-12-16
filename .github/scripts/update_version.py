import re
import sys


def update_version_in_setup(version):
    with open('../../setup.py', 'r') as file:
        setup_content = file.read()

    # Regex to find the version line
    version_line_regex = r"version='[\d\.]+'"
    new_version_line = f"version='{version}'"

    # Replace the version line
    updated_setup_content = re.sub(version_line_regex, new_version_line, setup_content)

    with open('../../setup.py', 'w') as file:
        file.write(updated_setup_content)


if __name__ == '__main__':
    new_version = sys.argv[1]
    update_version_in_setup(new_version)
