'''
        ____  ________  ________    _____   ________
       / __ \/  _/ __ \/ ____/ /   /  _/ | / / ____/
      / /_/ // // /_/ / __/ / /    / //  |/ / __/   
     / ____// // ____/ /___/ /____/ // /|  / /___   
    /_/   /___/_/   /_____/_____/___/_/ |_/_____/   

    A short demonstration of the framework.

'''


from pipeline import Pipeline
from pipeline.components.response import Response, JSONResponse


app = Pipeline()

@app.get('/')
def id(req):
    return Response('Hello route!')

@app.get('/users/(id)')
def id(req):
    return Response(req.params['id'])


app.run()