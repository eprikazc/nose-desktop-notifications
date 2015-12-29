from setuptools import setup, find_packages
setup(
    name = "nose-desktop-notifications",
    version = "0.1",
    packages=['nose_desktop_notifications'],
    # install_requires=[
    #     '',
    # ],
    entry_points={
        # 'nose.plugins.0.10': [
        'nose.plugins': [
            'nose_desktop_notifications = nose_desktop_notifications:DesktopNotificationPlugin',
        ]
    },
)