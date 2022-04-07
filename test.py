'''
        ____  ________  ________    _____   ________
       / __ \/  _/ __ \/ ____/ /   /  _/ | / / ____/
      / /_/ // // /_/ / __/ / /    / //  |/ / __/   
     / ____// // ____/ /___/ /____/ // /|  / /___   
    /_/   /___/_/   /_____/_____/___/_/ |_/_____/   
       ___  ___  __  ____ _________  ____________________
      / _ )/ _ \/ / / / //_/ __/ _ \/_  __/ __/ __/_  __/
     / _  / , _/ /_/ / ,< / _// , _/ / / / _/_\ \  / /   
    /____/_/|_|\____/_/|_/___/_/|_| /_/ /___/___/ /_/                                                                         

    Skriv kode som løser hvert scenario, bruk API 
    dokumentasjonen i API.txt, docstrings og type hints 
    som hjelp. Hvis dere står helt fast, spør utvikler.

    Anbefaler å bruke Postman, Insomnia eller Thunder 
    Client i VS Code til å teste endepunktene.

    Lykke til!
'''

from pipeline import Pipeline, Response, JSONResponse, JSONParser, TemplateResponse, Error

"""
SCENARIO 1

Lag en webapplikasjon på port 3000 med et endepunkt “/”, 
som returnerer teksten: “Hello World!”.
"""

app = Pipeline()

@app.get('/')
def index_view(req):
    return Response('Hello World!')

"""
SCENARIO 2

Lag et endepunkt “/users” som returnerer en liste av brukere, 
i form av et array av json objekter.
"""

users = [{'name': 'Thomas'}, {'name': 'Arthur'}]

@app.get('/users')
def users_view(req):
    return JSONResponse(users)

"""
SCENARIO 3

Lag et endepunkt “/user” med metode “post”, som tar imot en 
bruker og legger den inn i en liste av brukere. Når brukeren er 
lagt til, skal endepunktet returnere teksten “User created!” og 
statuskoden 201. Brukeren er et json objekt.
"""

@app.post('/users')
def create_user(req):
    user = JSONParser.run(req.body)
    users.append(user)
    return Response('User created!', 201)

"""
SCENARIO 4

Lag et dynamisk endepunkt “/users/(index)” som tar imot en 
variabel “index” fra nettadressen, og returnerer en bruker fra 
en liste av brukere med korresponderende index. Brukeren er et 
json objekt.
"""

@app.get('/users/(index)')
def read_users(req):
    index = int(req.params['index'])
    return JSONResponse(users[index])

"""
SCENARIO 5

Lag et endepunkt “/search” som henter ut query parameteret “q” 
fra nettadressen (?q=), og returnerer teksten: “You searched 
for (q)”.
"""

@app.get('/search')
def search_view(req):
    q = req.query['q']
    return Response(f'You searched for {q}')

"""
SCENARIO 6

Lag to endepunkter “/pay” og “/receipt”, hvor det først 
endepunktet omdirigerer brukeren til det andre. Endepunkt 
“/receipt” skal returnere teksten: “Here is your receipt!”.
"""

@app.get('/pay')
def pay_view(req):
    res = Response()
    res.redirect('/receipt')
    return res

@app.get('/receipt')
def receipt_view(req):
    return Response('Here is your receipt!')

"""
SCENARIO 7

Lag et endepunkt “/product” som lagrer en cookie hos 
klienten, med navn “product” og verdien “visited”. 
"""

@app.get('/product')
def product_view(req):
    res = Response()
    res.set_cookie('product', 'visited')
    return res

@app.get('/delete')
def x(req):
    res = Response()
    res.remove_cookie('product')
    return res

"""
SCENARIO 8

Lag et endepunkt “/” som returnerer en html fil “index.html”, 
med innhold: “<h1>Hello {name}!</h1>”, hvor “name” er en 
injisert variabel som skal settes til “Armin”.
"""

@app.get('/')
def index_view(req):
    return TemplateResponse('index.html', {'name': 'Armin'})

"""
STARTING THE APP FOR ALL SCENARIOS
ON PORT 3000
"""

app.run()