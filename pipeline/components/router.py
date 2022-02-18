class Router:
    def __init__(self) -> None:
        self.routes = []

    def add_route(self, pattern, handler):
        self.routes.append((pattern, handler))

    def match(self, path):
        for (pattern, handler) in self.routes:
            this_pattern = pattern.split('/')
            this_path = path.split('/')

            if len(this_path) == len(this_pattern):
                args = []

                for i, key in enumerate(this_pattern):
                    if key.startswith(':'):
                        args.append(this_path[i])

                    elif key != this_path[i]:
                        break

                    if i == len(this_pattern) - 1:
                        return (handler, tuple(args))