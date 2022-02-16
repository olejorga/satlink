from pipeline import Pipeline
from pipeline.responses import Response, TEXTResponse, JSONResponse


users = [
    {'name': 'Armin'},
    {'name': 'Sebastian'}
]

app = Pipeline()

@app.post('/users')
def create_user():
    return TEXTResponse('Hello World!')

@app.get('/users')
def read_all_users():
    return Response("Hello World", )

@app.patch('/users/<id>')
def update_user(req):
    pass

@app.delete('/users/<id>')
def delete_user(req):
    pass

app.run()