from setuptools import setup, find_packages
import sys

# Define OS-specific dependencies
windows_specific = ['pygetwindow', 'pywinauto']
mac_specific = ['pyobjc-framework-Quartz', 'pyobjc-framework-Cocoa']
linux_specific = ['python-xlib']

# Select dependencies based on the platform
if sys.platform.startswith('win'):
    required = windows_specific
if sys.platform.startswith('darwin'):
    required = mac_specific
elif sys.platform.startswith('linux'):
    required = linux_specific
else:
    required = []

common_requirements = [

]

setup(
    name='habittracker',
    version='0.1.0',
    author='Zeyad Rashed',
    author_email='zrashed02@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=common_requirements + required,
    description='A cross-platform application for tracking active application usage',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/notzune/habit-tracker',
    classifiers=[
        # Classifiers help users find your project by categorizing it.
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OSX and Linux',
    ],
    entry_points={
        'console_scripts': [
            'habittracker=habittracker.__main__:main',
        ],
    },
)
