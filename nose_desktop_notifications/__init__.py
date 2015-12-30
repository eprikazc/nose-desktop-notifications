from nose.plugins import Plugin
import notify2

notify2.init('')


class DesktopNotificationPlugin(Plugin):
    name = 'dn'
    def finalize(self, result):
        if result.wasSuccessful():
            subj = 'Nose tests passed'
            body = 'Run: %s' % result.testsRun
        else:
            subj = 'Nose tests failed'
            body = 'Run: %s\nFailed: %s' % (
                result.testsRun,
                len((result.errors + result.failures)))
        show_desktop_notification(subj, body, result.wasSuccessful())


def show_desktop_notification(subj, body, is_success):
    # TODO: add support for more operating systems:
    icon = 'stock_yes' if is_success else 'stock_no'
    notify2.Notification(subj, body, icon).show()
