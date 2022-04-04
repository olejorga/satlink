'''
        ____  ________  ________    _____   ________
       / __ \/  _/ __ \/ ____/ /   /  _/ | / / ____/
      / /_/ // // /_/ / __/ / /    / //  |/ / __/   
     / ____// // ____/ /___/ /____/ // /|  / /___   
    /_/   /___/_/   /_____/_____/___/_/ |_/_____/   

    A short demonstration of the framework.

'''
from pipeline import Pipeline, Response, JSONParser

app = Pipeline()

@app.get('/')
def index(req):
    return Response('Hello World!')


@app.post('/')
def x(req):
    d = JSONParser.run(req.body)
    return Response(d['name'])

app.run()