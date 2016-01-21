nose-desktop-notifications
==========================
Desktop notifications to show nose test run results. Tested in Ubuntu 15.10, but it should work with any desktop environment supporting D-BUS.

Inspired by https://github.com/dbader/pytest-osxnotify

Usage
-----
```shell
$ pip install git+https://github.com/posborne/dbus-python.git
$ pip install notify2
$ pip install git+https://github.com/eprikazc/nose-desktop-notifications.git
$ nosetests example_test.py --with-dn
```
