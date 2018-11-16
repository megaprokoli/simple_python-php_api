import requests

from php_api.php_array import PhpArray


class PhpInterface:

    def __init__(self, host):
        self.host = host

    def call(self, func, args=None):    # [(type, val), (type, val)]

        if args is not None:
            arg_str = ""

            for arg in args:
                arg_str += str(arg[0]) + "#" + str(arg[1]) + '|'

            response = requests.get(self.host, params={"data": func, "args": arg_str})
        else:
            response = requests.get(self.host,  params={"data": func})

        if response.status_code == 500:     # kinda catch exceptions
            return None

        resp = response.content.decode()
        array = PhpArray.create(resp)

        if array is None:
            return resp
        return array
