from pipeline import Pipeline
from pipeline.helpers import openers
from pipeline.helpers import wrappers

# Dummy database med brukere
users = []

# Lager en applikasjon med port 3000
app = Pipeline(port=3000) # <--- Kan angi port her

# Definerer en kontroller
def read_user_by_id(req):
    for user in users:
        if user["id"] == req.path["id"]:
            return wrappers.json(user)

# Binder kontrolleren til endepunktet
app.get("/users/[id]", read_user_by_id)

# Starter applikasjonen med port 3000
app.run(3000) # <--- Kan også angi port her