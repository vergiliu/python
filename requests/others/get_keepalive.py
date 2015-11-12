import requests

applications = {
    'pam': 'localhost',
    'cha': 'localhost',
    'ccs': '127.0.0.1',
    'iup': 'monkey',
    'error': 'localhost',
    'cpa': 'localhost',
}


class KeepAliveChecker:
    def __init__(self, silent=True):
        """
        silent - enable if only OK applications should be printed and no other data
        """
        self.silent = silent
        self.validated = {}

    def create_location(self, app, loc):
        return 'http://{}:8888/{}/keepalive.jsp'.format(loc, app)

    def check_application(self, application, location):
        url = self.create_location(application, location)
        if not self.silent:
            print('checking application {} for {}'.format(application, url))
        try:
            reply = requests.get(url, timeout=2)
            if reply.status_code == requests.codes.ok:
                self.validated[application] = True
            else:
                self.validated[application] = False
        except requests.exceptions.ConnectionError as e:
            print(e)
            self.validated[application] = False

    def display_validated(self):
        for app_name, status in self.validated.items():
            if status:
                print('{} - OK'.format(app_name))
            elif not self.silent:
                print('{} - NOT_OK'.format(app_name))

if __name__ == '__main__':
    kc = KeepAliveChecker(silent=False)

    for app, location in applications.items():
        kc.check_application(app, location)

    kc.display_validated()