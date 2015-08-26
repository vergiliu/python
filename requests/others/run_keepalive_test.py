import requests
import unittest
from httmock import urlmatch, HTTMock
from get_keepalive import KeepAliveChecker

class KeepAliveTests(unittest.TestCase):
    @urlmatch(netloc=r'.*$', path=r'^.*keepalive.jsp$')
    def mock_valid(self, url, request):
        return 'OK'

    @urlmatch(netloc=r'.*$', path=r"^.*error.*$")
    def mock_invalid(self, url, request):
        r = requests.Response()
        r.status_code = 400
        r._content = 'Bad request'
        return r

    def test_validate_running_application(self):
        application = 'test'
        with HTTMock(self.mock_valid):
            kc = KeepAliveChecker(silent=False)
            kc.check_application(application, "somewhere")
        self.assertTrue(kc.validated[application])

    def test_validate_stopped_application(self):
        application = 'error'
        kc = KeepAliveChecker()
        with HTTMock(self.mock_invalid):
            kc.check_application(application, 'localhost')
        self.assertFalse(kc.validated[application])

    def skip_test_2(self):
        print('test2')

if __name__ == '__main__':
    unittest.main()

    # @urlmatch(netloc=r'(.*\.)?google\.com$', path=r'^/$')
    # def google_mock(self, url, request):
    #     return 'Hello from Google'
    #
    # def skip_test_httmock_magic(self):
    #     with HTTMock(self.google_mock):
    #         r = requests.get('http://www.google.com')
    #     self.assertEqual(200, r.status_code)
    #     print(r)