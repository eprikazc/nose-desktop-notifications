nose-desktop-notifications
==========================
Desktop notifications to show nose test run results. Currently works in Ubuntu only.

Inspired by https://github.com/dbader/pytest-osxnotify

Usage
-----
```shell
$ pip install git+https://github.com/posborne/dbus-python.git
$ pip install notify2
$ pip install git+https://github.com/eprikazc/nose-desktop-notifications.git
$ nosetests example_test.py --with-dn
```
