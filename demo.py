'''
        ____  ________  ________    _____   ________
       / __ \/  _/ __ \/ ____/ /   /  _/ | / / ____/
      / /_/ // // /_/ / __/ / /    / //  |/ / __/   
     / ____// // ____/ /___/ /____/ // /|  / /___   
    /_/   /___/_/   /_____/_____/___/_/ |_/_____/   

    A short demonstration of the framework.

'''


from pipeline import Pipeline
from pipeline.components.response import Response, JSONResponse, TemplateResponse


users = [{'name': 'Jon'}, {'name': 'Eric'}]

app = Pipeline()


@app.get('/')
def index_view(req):
    return TemplateResponse('index.html', {'name': 'Adrian'})


@app.get('/users')
def read_users(req):
    print("??")
    return JSONResponse(users)

@app.get('/users/(name)')
def read_user(req):
    print(req.params['name'])
    user = list(filter(lambda u: u['name'] == req.params['name'], users))[0]
    return JSONResponse(user)


app.run()