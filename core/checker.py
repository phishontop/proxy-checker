from .httpzoom import Client


class CheckerError(Exception):
    pass


class Checker:

    def __init__(self, proxy, timeout=5):
        self.proxy = proxy
        self.timeout = timeout

    def check(self):
        try:
            client = Client(
                host="httpbin.org",
                proxy=self.proxy,
                timeout=self.timeout
            )
            client.get(resource="/ip")
            return True
        except:
            return False

    @property
    def proxy(self):
        return self._proxy

    @proxy.setter
    def proxy(self, value):
        if value.count(".") == 3 and value.count(":") == 1:
            self._proxy = value
        else:
            raise CheckerError("The Proxy has an invalid format")
