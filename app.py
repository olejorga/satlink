'''

    PIPELINE DEMO

    A short demonstration of the framework.

'''

# STEP 1: Import pipeline
from pipeline import Pipeline
from pipeline.components.response import Response

# STEP 2: Create a dummy user database
users = [
    {'name': 'Armin'},
    {'name': 'Sebastián'}
]

# STEP 3: Create an app
app = Pipeline()


# STEP 4: Add a dynamic route as a GET method - with a handler
@app.get('/users/:index')
def read_user_by_index(req):
    try:
        return Response(str(users[int(req.params['index'])]))
    except:
        return Response('User not found', 500)


# STEP 5: Add a route as a GET method - with a handler
@app.get('/users')
def read_all_users(req):
    return Response(str(users))

@app.get('/hello/:name/and/:other/')
def greet(req):
    return Response(f"Hello {req.params['name']}! ... and {req.params['other']}!")


# STEP 6: Add a route as a POST method - with a handler
'''
@app.post('/users')
def create_user(ctx):
    user = ctx.body
    users.append(user)

    return Response('User was created', 201)
'''


# STEP 7: Start the app
app.run()