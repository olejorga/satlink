'''

    PIPELINE DEMO

    A short demonstration of the framework.

'''


# STEP 1: Import pipeline
import json
from pipeline import Pipeline
from pipeline.components.response import Response


# STEP 2: Create a dummy user database
users = [
    {'name': 'Armin'},
    {'name': 'Sebastián'}
]

# STEP 3: Create an app
app = Pipeline()


# STEP 2: Add a route as a GET method - with a handler
@app.get('/users')
def read_all_users(req):
    return Response(str(users))


# STEP 5: Add a dynamic route as a GET method - with a handler
@app.get('/users/:index')
def read_user_by_index(req):
    try:
        return Response(str(users[int(req.params['index'])]))
    except:
        return Response('User not found', 500)


# STEP 6: Add a route as a POST method - with a handler
@app.post('/users')
def create_user(req):
    user = json.loads(req.body)
    users.append(user)

    return Response('User created', 201)


# STEP 7: Add a route as a PUT method - with a handler
@app.put('/users/:index')
def create_user(req):
    user = json.loads(req.body)
    users[int(req.params['index'])] = user

    return Response('User updated')


# STEP 8: Add a route as a DELETE method - with a handler
@app.delete('/users/:index')
def create_user(req):
    users.remove(users[int(req.params['index'])])
    return Response('User deleted')


# STEP 7: Start the app
app.run()