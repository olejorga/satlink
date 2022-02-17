from re import match as RE_MATCHER


class Router:
    def __init__(self) -> None:
        self.routes = []

    def add_route(self, pattern, handler):
        self.routes.append((pattern, handler))

    def match(self, path):
        for (pattern, handler) in self.routes:
            m = RE_MATCHER(pattern, path)
            if m:
                return (handler, m.groups())
            print('SHIT!')