class T:
    @staticmethod
    def controller(ctx: dict) -> int:
        pass

class Pipeline:

    def __init__(self, port: int) -> None:
        pass
    
    def get(self, path: str, controller: T.controller) -> str:
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

    def run(self, port: int) -> bool:
        pass