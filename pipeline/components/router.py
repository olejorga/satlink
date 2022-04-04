from shutil import ExecError
from typing import Callable


class Router:
    def __init__(self) -> None:
        self.__routes = []

    def add_route(self, pattern: str, handler: Callable) -> None:
        self.__routes.append((pattern, handler))

    def match(self, path: str) -> tuple:
        path = path[:-1] if path.endswith('/') and path != "/" else path

        for (pattern, handler) in self.__routes:
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
                        return (handler, params)
                else:
                    break
                continue
        
        raise Exception(f"No controller found for route {path}")