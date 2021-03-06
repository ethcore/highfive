from __future__ import absolute_import

from eventhandler import EventHandler

NO_MODIFY_CSS_TESTS_MSG = '''This pull request modifies the contents of
`tests/wpt/css-tests/`, which are overwriten occasionally whenever the
directory is synced from upstream.'''


class NoModifyCSSTestsHandler(EventHandler):
    DIR_TO_CHECK = "tests/wpt/css-tests"

    def on_pr_opened(self, api, payload):
        for filepath in api.get_changed_files():
            if self.DIR_TO_CHECK in filepath:
                self.warn(NO_MODIFY_CSS_TESTS_MSG)
                break

handler_interface = NoModifyCSSTestsHandler
