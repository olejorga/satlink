from typing import Callable
from .error import Error


class Router:
    def __init__(self) -> None:
        self.__routes = []

    def add_route(self, pattern: str, controller: Callable) -> None:
        self.__routes.append((pattern, controller))

    def match(self, path: str) -> tuple:
        path = path[:-1] if path.endswith('/') and path != "/" else path

        for (pattern, controller) in self.__routes:
            keys = pattern.split('/')[1:]
            values = path.split('/')[1:]

            if len(keys) == len(values):
                params = {}

                for i, key in enumerate(keys):
                    if key.startswith('(') and key.endswith(')'):
                        params[key[1:-1]] = values[i]

                    elif key != values[i]:
                        break

                    if i == len(keys) - 1:
                        return (controller, params)
                else:
                    break
                continue
        
        raise Error(404, f"No controller found for route {path}")