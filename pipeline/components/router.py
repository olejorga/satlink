class Router:
    def __init__(self) -> None:
        self.routes = []

    def add_route(self, pattern, handler):
        self.routes.append((pattern, handler))

    def match(self, path):
        path = path[:-1] if path.endswith('/') and path != "/" else path

        for (pattern, handler) in self.routes:
            pattern = pattern[:-1] if pattern.endswith('/') and pattern != "/" else pattern
            pattern = pattern.split('/')
            current_path = path.split('/')

            if len(current_path) == len(pattern):
                args = {}

                for i, key in enumerate(pattern):
                    if key.startswith(':'):
                        args[key[1:]] = current_path[i]

                    elif key != current_path[i]:
                        break

                    if i == len(pattern) - 1:
                        return (handler, args)