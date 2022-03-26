from typing import Callable


class Router:
    def __init__(self) -> None:
        self.__routes = []

    def add_route(self, pattern: str, handler: Callable) -> None:
        self.__routes.append((pattern, handler))

    def match(self, path: str) -> tuple:
        path = path[:-1] if path.endswith('/') and path != "/" else path

        for (pattern, handler) in self.__routes:
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