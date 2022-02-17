class Context:
    
    def __init__(
        self, 
        body:str = '', 
        path: dict = {}, 
        query: dict = {}, 
        headers: dict = {}
    ) -> None:
        self.body = body
        self.path = path
        self.query = query
        self.headers = headers