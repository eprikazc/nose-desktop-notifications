from setuptools import setup

setup(
    name = "nose-desktop-notifications",
    version = "0.1",
    packages=['nose_desktop_notifications'],
    entry_points={
        'nose.plugins': [
            'nose_desktop_notifications = nose_desktop_notifications:DesktopNotificationPlugin',
        ]
    },
)