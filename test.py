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

    Skriv kode som løser hvert scenario, lykke til!
'''

from pipeline import Pipeline, Response

"""
SCENARIO 1

Lag en webapplikasjon på port 3000 med et endepunkt “/”, 
som returnerer teksten: “Hello World!”.
"""

# KODE

"""
SCENARIO 2

Lag et endepunkt “/users” som returnerer en liste av brukere, 
i form av et array av json objekter.
"""

# KODE

"""
SCENARIO 3

Lag et endepunkt “/user” med metode “post”, som tar imot en 
bruker og legger den inn i en liste av brukere. Når brukeren er 
lagt til, skal endepunktet returnere teksten “User created!” og 
statuskoden 201. Brukeren er et json objekt.
"""

# KODE

"""
SCENARIO 4

Lag et dynamisk endepunkt “/users/(index)” som tar imot en 
variabel “index” fra nettadressen, og returnerer en bruker fra 
en liste av brukere med korresponderende index. Brukeren er et 
json objekt.
"""

# KODE

"""
SCENARIO 5

Lag et endepunkt “/search” som henter ut query parameteret “q” 
fra nettadressen (?q=), og returnerer teksten: “You searched 
for (q)”.
"""

# KODE 

"""
SCENARIO 6

Lag to endepunkter “/pay” og “/receipt”, hvor det først 
endepunktet omdirigerer brukeren til det andre. Endepunkt 
“/receipt” skal returnere teksten: “Here is your receipt!”.
"""

# KODE 

"""
SCENARIO 7

Lag et endepunkt “/product” som lagrer en cookie hos 
klienten, med navn “product” og verdien “visited”. 
"""

# KODE

"""
SCENARIO 8

Lag et endepunkt “/” som returnerer en html fil “index.html”, 
med innhold: “<h1>Hello {name}!</h1>”, hvor “name” er en 
injisert variabel som skal settes til “Armin”.
"""

# KODE